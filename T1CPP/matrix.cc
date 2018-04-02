#ifndef MATRIX_CC
#define MATRIX_CC
#include <vector>



class Matrix
{
public:
	Matrix(int _rows, int _cols): rows(_rows), cols(_cols) {
		std::vector<double> m(_rows *_cols);

		rawMatrix = m;
	}
	int getRows() const{
		return this->rows;
	}
	int getCols() const{
		return this->cols;
	}
	void setValue(int row, int col, double value) {
		rawMatrix.at(row*cols + col) = value;
	}
	double getValue(int row, int col) {
		return rawMatrix[row*cols + col];
	}

	double &operator()(int i, int j) {
	    return rawMatrix[i*cols + j];
	}

	double operator()(int i, int j) const {
	    return rawMatrix[i*cols + j];
	}
	Matrix& operator*=(const Matrix& rhs) {
		Matrix m{this->rows, rhs.cols};
		for (int i = 0; i < this->rows; ++i) {
			for (int j = 0; j < rhs.getCols(); ++j) {
				m.setValue(i, j, 0);
				for (int k = 0; k < rhs.getRows(); ++k) {
					m.setValue(i, j, (this->getValue(i,k) * rhs(k,j)) + m.getValue(i,j));
				}
			}
		}
		return *this = m;
	}
	Matrix& operator*=(double scalar) {
		Matrix m{this->rows, this->cols};
		for (int i = 0; i < this->rows; ++i) {
			for (int j = 0; j < this->cols; ++j) {
				double res = this->getValue(i, j) * scalar;
			}
		}
		return *this = m;
	}
	static Matrix identidade(int n) {
		Matrix m(n,n);
		for(int i = 0; i < n;i++) {
			for(int j = 0; j < n;j++) {
				m.setValue(i,j,0);
				if(i==j) m.setValue(i,j,1);
			}
		}
		return m;
	}
	~Matrix() {

	}

private:
	int rows;
	int cols;
	std::vector<double> rawMatrix;
};

inline Matrix operator*(Matrix a, const Matrix& b) {
 	return a *= b;
}

inline Matrix operator*(Matrix a, double v) {
 	return a *= v;
}


#endif