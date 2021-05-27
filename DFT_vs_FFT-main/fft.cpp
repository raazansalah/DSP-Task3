#include <math.h>
#include <complex>
#include <vector>
#include <iostream>
#include <iomanip>

extern "C"
{
    void C_dft(double *i_real, double *i_imag, int i_size, double **o_real, double **o_imag, int *o_size);
    void C_fft(double *i_real, double *i_imag, int i_size, double **o_real, double **o_imag, int *o_size);
}

void C_dft(double *i_real, double *i_imag, int i_size, double **o_real, double **o_imag, int *o_size)
{
    double real_sum, imag_sum;
    //Determine number of samples
    int N = i_size;
    //Allocate memory for the output
    *o_real = new double[N];
    *o_imag = new double[N];
    *o_size = N;
    //Loop through each k
    for (int k = 0; k < N; k++)
    {
        real_sum = 0, imag_sum = 0;
        //loop through each n
        for (int n = 0; n < N; n++)
        {
            double real_part = cos(((2 * M_PI) / N) * k * n);
            double imag_part = sin(((2 * M_PI) / N) * k * n);

            real_sum += i_real[n] * real_part + i_imag[n] * imag_part;
            imag_sum += i_real[n] * -imag_part + i_imag[n] * real_part;
        }
        (*o_real)[k] = real_sum, (*o_imag)[k] = imag_sum;
    }
}

void C_fft(double *i_real, double *i_imag, int i_size, double **o_real, double **o_imag, int *o_size)
{
    //find the number of samples
    int N = i_size;
    *o_size = N;

    *o_real = new double[N];
    *o_imag = new double[N];
    //exectute the end of the recursive even/odd splits once we only have one sample
    if (i_size == 1)
    {
        (*o_real)[0] = i_real[0];
        (*o_imag)[0] = i_imag[0];
        return;
    }
    //split the samples into even and odd subsums
    //find half the total number of samples
    int M = N / 2;
    //declare an even and arrays
    double Xeven_real[M];
    double Xeven_imag[M];
    double Xodd_real[M];
    double Xodd_imag[M];
    //input the even and odd samples
    for (int i = 0; i < M; i++)
    {
        Xeven_real[i] = i_real[2 * i], Xeven_imag[i] = i_imag[2 * i];
        Xodd_real[i] = i_real[2 * i + 1], Xodd_imag[i] = i_imag[2 * i + 1];
    }

    double *Feven_real = new double[M];
    double *Feven_imag = new double[M];
    double *Fodd_real = new double[M];
    double *Fodd_imag = new double[M];
    int Feven_size;
    int Fodd_size;
    //perform the recursive FFT operation on the odd and even sides
    C_fft(Xeven_real, Xeven_imag, M, (double **)(&Feven_real), (double **)(&Feven_imag), &Feven_size);
    C_fft(Xodd_real, Xodd_imag, M, (double **)(&Fodd_real), (double **)(&Fodd_imag), &Fodd_size);
    /* END OF RECURSION */
    //combine the values found
    for (int k = 0; k < M; k++)
    {
        double polar_real = cos(-2 * M_PI * k / N);
        double polar_imag = sin(-2 * M_PI * k / N);
        //for each split set, we need to multiply a k-dependent complex number by the odd subsum
        double cmplxexpo_real = polar_real * Fodd_real[k] - polar_imag * Fodd_imag[k];
        double cmplxexpo_imag = polar_real * Fodd_imag[k] + polar_imag * Fodd_real[k];

        (*o_real)[k] = Feven_real[k] + cmplxexpo_real;
        (*o_imag)[k] = Feven_imag[k] + cmplxexpo_imag;
    //everytime you add pi, exponential changes sign
        (*o_real)[k + M] = Feven_real[k] - cmplxexpo_real;
        (*o_imag)[k + M] = Feven_imag[k] - cmplxexpo_imag;
    }

    delete[] Feven_real;
    delete[] Feven_imag;
    delete[] Fodd_real;
    delete[] Fodd_imag;
}

// int main()
// {

//     int i_size = 4;
//     double i_real[] = {0, 1, 2, 3};
//     double i_imag[] = {0, 0, 0, 0};

//     double *o_real, *o_imag;
//     int o_size;

//     C_fft(i_real, i_imag, i_size, &o_real, &o_imag, &o_size);

//     for (int i = 0; i < 4; i++)
//         std::cout << "(" << o_real[i] << "," << o_imag[i] << ")" << std::endl;
// }