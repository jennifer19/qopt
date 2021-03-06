#ifndef _QIEA2_H
#define _QIEA2_H 1

#include "framework.h"

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <limits>

class QIEA2 {

	public:

		typedef double DTYPE;

		DTYPE *Q;    // [popsize,N] -- quantum population
		DTYPE *P;    // [K,N]       -- observed classical population  (denoted E in iQIEA)
		DTYPE *P_old; // [K,N]       -- old observed classical population  (denoted E in iQIEA)

		int t;

		DTYPE (*bounds)[2];
		int popsize; // |Q|
		int chromlen; // N
		int K; // |P| >= popsize

		float delta;
		float XI;

		DTYPE *fvals;
		DTYPE bestval;
		DTYPE *best;
		// DTYPE (*bestq)[2];

		Problem<DTYPE,DTYPE> *problem;

		QIEA2(int chromlen, int popsize, int K = -1) : popsize(popsize), chromlen(chromlen), K(K) {
			if (K == -1) {
				this->K = popsize;
			}
			printf("QIEA2::QIEA2 constructor (N=%d |Q|=%d K=%d)\n", chromlen, popsize, this->K);
			assert(chromlen % 2 == 0);

			problem = NULL;
			bestval = std::numeric_limits<DTYPE>::max();
			delta = .9995;
			XI = .9;

			Q = new DTYPE[5 * chromlen / 2 * popsize];
			P = new DTYPE[this->K * chromlen];
			P_old = new DTYPE[this->K * chromlen];
			fvals = new DTYPE[this->K];
			bounds = new DTYPE[chromlen][2];
			best = new DTYPE[chromlen];
			// bestq = new DTYPE[chromlen][2];
		}

		~QIEA2() {
			delete [] Q;
			delete [] P;
			delete [] P_old;
			delete [] bounds;
			delete [] best;
			delete [] fvals;
			// delete [] bestq;
		}

		// the whole algorithm in C++
		void run();

		// elementary operations
		void initialize();
		void observe();
		void storebest();
		void evaluate();
		void update();
		// void recombine();
		// void catastrophe();

		void crossover();
		void mutate();

		DTYPE LUT(DTYPE alpha, DTYPE beta, DTYPE alphabest, DTYPE betabest);

};

inline double box_muller() {
	double u1 = 1.0 * rand() / RAND_MAX;
	double u2 = 1.0 * rand() / RAND_MAX;
	double result = sqrt(-2.*log(u1)) * cos(2.*M_PI*u2);
	return result;
}

inline double sign(double x) {
	if (x > 0)
		return 1;
	else if (x < 0)
		return -1;
	else
		return 0;
}

#endif
