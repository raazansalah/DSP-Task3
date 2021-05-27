#include <math.h>
#include <complex>
#include <vector>
#include <iostream>
#include <iomanip>

extern "C"
{
    std::vector<std::complex<double>> dft(std::vector<std::complex<double>> X);    
    std::vector<std::complex<double>> FFT(std::vector<std::complex<double>> &samples);
}


std::vector<std::complex<double>> dft(std::vector<std::complex<double>> X)
{
    //Determine number of samples
    int N = X.size();
    int K = N;
    //Allocate memory for internals
    std::complex<double> intSum;
    //Allocate memory for output
    std::vector<std::complex<double>> output;
    output.reserve(K);
    //Loop through each k
    for (int k = 0; k<K; k++)
    {
        //loop through each n
        intSum = std::complex<double>(0, 0);
        for( int n=0; n<N; n++)
        {
            double realPart = cos(((2*M_PI)/N) * k * n);
            double imagPart = sin(((2*M_PI)/N) * k * n);
            std::complex<double> w (realPart, -imagPart);
            intSum += X[n] * w;
        }
        output.push_back(intSum);
    }
    return output;
}
std::vector<std::complex<double>> FFT(std::vector<std::complex<double>> &samples)
{
    //find the number of samples
    int N = samples.size();
    //exectute the end of the recursive even/odd splits once we only have one sample
    if(N == 1)
    {
        return samples;
    }
    //split the samples into even and odd subsums
    //find half the total number of samples
    int M = N/2;
    //declare an even and odd complex vector
    std::vector<std::complex<double>> Xeven(M, 0);
    std::vector<std::complex<double>> Xodd(M, 0);
    //input the even and odd samples into respective vectors
    for( int i =0; i!=M; i++)
    {
        Xeven[i] = samples[2*i];
        Xodd[i] = samples[2*i+ 1];
    }
    //perform the recursive FFT operation on the odd and even sides
    std::vector<std::complex<double>> Feven(M, 0);
    Feven = FFT(Xeven);
    std::vector<std::complex<double>> Fodd(M, 0);
    Fodd = FFT(Xodd);
    /* END OF RECURSION */
    //declare vector of frequency bins 
    std::vector<std::complex<double>> freqbins(N,0);
    //combine the values found
    for(int k=0; k!=N/2; k++)
    {
        //for each split set, we need to multiply a k-dependent complex number by the odd subsum
        std::complex<double> cmplxexponential = std::polar(1.0, -2*M_PI*k/N)* Fodd[k];
        freqbins[k] = Feven[k] + cmplxexponential;
        //everytime you add pi, exponential changes sign
        freqbins[k+N/2] = Feven[k] - cmplxexponential;
    }
    return freqbins;

}
int main()
{
    //create a test signal
    int N = 1024;
    std::vector<std::complex<double>> signal;
    signal.reserve(N);
    double sigK = 3.0;
    //double sigPhase = M_PI/ 4.0;
    double sigPhase = 0.0;
    for( int x=0; x<N; ++x)
    {
        auto currentSample = std::complex<double>
        (cos((2*M_PI/static_cast<double>(N)) *
        sigK * static_cast<double>(x) + sigPhase), 0.0);
        signal.push_back(currentSample);
    }
    //compute the DFT
    std::vector<std::complex<double>> Fx = dft(signal);
    //display the first six values (real and imaginary components)
    std::cout << "****" << std::endl;
    std::cout << "First 6 samples of the output..." << std::endl;
    std::cout << "\n" << "k\t" << std::setw(12)
    << "Real\t" << std::setw(12) << "Imag" << std::endl;
    for(int i=0; i<6; ++i)
    {
        std::cout << i << "\t "
        << std::setw(12) << Fx[i].real() / static_cast<double>(N) << "\t"
        << std::setw(12) << Fx[i].imag() / static_cast<double>(N) << std::endl;
    }
    
    //compute the FFT
    std::vector<std::complex<double>> FFTx = FFT(signal);
    //display the first six values (real and imaginary components)
    std::cout << "****" << std::endl;
    std::cout << "First 6 samples of the output..." << std::endl;
    std::cout << "\n" << "k\t" << std::setw(12)
    << "Real\t" << std::setw(12) << "Imag" << std::endl;
    for(int i=0; i<6; ++i)
    {
        std::cout << i << "\t "
        << std::setw(12) << FFTx[i].real() / static_cast<double>(N) << "\t"
        << std::setw(12) << FFTx[i].imag() / static_cast<double>(N) << std::endl;
    }
    return 0;
}