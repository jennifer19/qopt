__constant__ int nreal;
__constant__ int nfunc;

// wszystko ponizsze, co jest stale, chyba powinno byc w constant (wspolne dla wszystkich watkow)
__device__ double C;  // const?
__device__ double global_bias;  // const?
/*
__device__ double *trans_x; // RW (te chyba powinny byc w shared, ale osobne dla kazdego watku,
__device__ double *temp_x1; // RW wiec to chyba powinno byc tablicami 2d)
__device__ double *temp_x2; // RW (jednak w shared to sie nie zmiesci: 50 osobnikow * 50 dim * 8bytes = 20 KB)
__device__ double *temp_x3; // RW (wychodzi na to, ze musi byc w global)
__device__ double *temp_x4; // RW
__device__ double *norm_x;  // RW
__device__ double *basic_f; // nfunc  RW (ok 4 KB w przypadku 50 osobnikow)
__device__ double *weight; // nfunc   RW
__device__ double *norm_f; // nfunc  RW
*/

__device__ double *sigma; // nfunc  // const? (4KB)
__device__ double *lambda; // nfunc  // const? (4KB)
__device__ double *bias; // nfunc  // const? (4KB)
__device__ double **o; // const? (nfunc x nreal) (maks 4 KB)
__device__ double **g; // const? (nreal x nreal) (20KB dla nreal 50)
__device__ double ***l;  // const? (nfunc x nreal x nreal) (maks 200 KB)

__device__ double *l_flat;


// for parallel execution
#define GTID ( blockIdx.y * blockDim.x + threadIdx.x )

__device__ double *g_trans_x; // RW (te chyba powinny byc w shared, ale osobne dla kazdego watku,
__device__ double *g_temp_x1; // RW wiec to chyba powinno byc tablicami 2d)
__device__ double *g_temp_x2; // RW (jednak w shared to sie nie zmiesci: 50 osobnikow * 50 dim * 8bytes = 20 KB)
__device__ double *g_temp_x3; // RW (wychodzi na to, ze musi byc w global)
__device__ double *g_temp_x4; // RW
__device__ double *g_norm_x;  // RW
__device__ double *g_basic_f; // nfunc  RW (ok 4 KB w przypadku 50 osobnikow)
__device__ double *g_weight; // nfunc   RW
__device__ double *g_norm_f; // nfunc  RW

#define trans_x (g_trans_x + nreal * GTID)
#define temp_x1 (g_temp_x1 + nreal * GTID)
#define temp_x2 (g_temp_x2 + nreal * GTID)
#define temp_x3 (g_temp_x3 + nreal * GTID)
#define temp_x4 (g_temp_x4 + nreal * GTID)
#define norm_x  (g_norm_x  + nreal * GTID)
#define basic_f (g_basic_f + nfunc * GTID)
#define weight  (g_weight  + nfunc * GTID)
#define norm_f  (g_norm_f  + nfunc * GTID)


__device__ double calc_sphere (double *x)
{
    int i;
    double res;
    res = 0.0;
    for (i=0; i<nreal; i++)
    {
        res += x[i]*x[i];
    }
    return (res);
}

__device__ double calc_schwefel (double *x)
{
    int i, j;
    double sum1, sum2;
    sum1 = 0.0;
    for (i=0; i<nreal; i++)
    {
        sum2 = 0.0;
        for (j=0; j<=i; j++)
        {
            sum2 += x[j];
        }
        sum1 += sum2*sum2;
    }
    return (sum1);
}

__device__ void transform (double *x, int count)
{
    int i, j;
    for (i=0; i<nreal; i++)
    {
        temp_x1[i] = x[i] - o[count][i];
    }
    for (i=0; i<nreal; i++)
    {
        temp_x2[i] = temp_x1[i]/lambda[count];
    }
    for (j=0; j<nreal; j++)
    {
        temp_x3[j] = 0.0;
        for (i=0; i<nreal; i++)
        {
            temp_x3[j] += g[i][j]*temp_x2[i];
        }
    }
    for (j=0; j<nreal; j++)
    {
        trans_x[j] = 0.0;
        for (i=0; i<nreal; i++)
        {
            // trans_x[j] += l[count][i][j]*temp_x3[i];
            trans_x[j] += l_flat[count * (nreal * nreal) + i * nreal + j] *temp_x3[i];
        }
    }
    return;
}

// F1
__global__ void calc_benchmark_func_f1(double *x, double *res)
{
    transform (x + nreal * GTID, 0);
    basic_f[0] = calc_sphere (trans_x);
    res[GTID] = basic_f[0] + bias[0];
}

// F2
__global__ void calc_benchmark_func_f2(double *x, double *res)
{
    transform (x + nreal * GTID, 0);
    basic_f[0] = calc_schwefel (trans_x);
    res[GTID] = basic_f[0] + bias[0];
}

// F3
__global__ void calc_benchmark_func_f3(double *x, double *res)
{
    int i;
    transform (x + nreal * GTID, 0);
    basic_f[0] = 0.0;
    for (i=0; i<nreal; i++)
    {
        basic_f[0] += trans_x[i]*trans_x[i]*pow(1.0e6,i/(nreal-1.0));
    }
    res[GTID] = basic_f[0] + bias[0];
}

__global__ void f(double *arg, double *result)
{
    result[threadIdx.x] = calc_sphere(arg);
    //result[threadIdx.x] = 1;
}

__global__ void test(double *result, double *o_out, double *g_out, double *l_out) {
    //MEM = *foo;
    //result[0] = sizeof(MEM_t);
    result[0] = l_flat[0];
    result[1] = C;
    result[2] = trans_x[0];
    result[3] = temp_x4[1];
    result[4] = norm_x[0];
    result[5] = norm_f[0];
    result[6] = o[1][0];
    result[7] = bias[0];

    for (int i = 0; i < nfunc; i++) {
        for (int j = 0; j < nreal; j++) {
            o_out[i * nreal + j] = o[i][j];
        }
    }

    for (int i = 0; i < nreal; i++) {
        for (int j = 0; j < nreal; j++) {
            g_out[i * nreal + j] = g[i][j];
        }
    }

    l_out[0] = 13;

    for (int i = 0; i < nfunc * nreal * nreal; i++) {
        l_out[i] = l_flat[i];
    }
}