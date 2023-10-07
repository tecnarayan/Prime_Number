#include <boost/multiprecision/cpp_int.hpp>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/uniform_int_distribution.hpp>
#include<bits/stdc++.h>

using namespace boost::multiprecision;


cpp_int modular_pow(cpp_int base, cpp_int exponent, cpp_int modulus) {
    if (modulus == 1) return 0;

    cpp_int result = 1;
    base = base % modulus;

    while (exponent > 0) {
        // If exponent is odd, multiply base with result
        if (exponent % 2 == 1) {
            result = (result * base) % modulus;
        }

        // Exponent must be even now
        exponent = exponent / 2;
        base = (base * base) % modulus;
    }

    return result;
}

bool detected_composite(cpp_int n){
    if(n%2 == 0) return true;

    cpp_int r , s;
    r = 0;

    cpp_int temp = n-1;

    while(true){
        if(temp%2 != 0)break;
        else{
            r+=1;
            temp /= 2;
        }
    }

    s = (n-1)/r;

    std::ifstream inputFile("prime-numbers.csv");
    std::string a_string;
    while(getline(inputFile , a_string)){

        cpp_int a(a_string);

        cpp_int alpha = modular_pow(a , s , n);
        if(alpha == 1 || alpha == (-1)) continue;

        for(cpp_int i = 1 ; i<= r ; i++){
            if(alpha == (-1) )break;
            if( alpha == 1) return true;
            if( i == r && alpha != 1) return true;
            alpha = (alpha * alpha) % n;
        }

    }
    return false;
}


cpp_int generateRandomCppInt(const cpp_int& min_value, const cpp_int& max_value) {
    boost::random::mt19937 rng; // Mersenne Twister random number generator
    boost::random::uniform_int_distribution<cpp_int> dist(min_value, max_value);
    return dist(rng);
}


cpp_int pollard_rho(cpp_int n){

    if( ! (detected_composite(n))) return n;

    cpp_int a = generateRandomCppInt(2 , n-1);
    cpp_int b = a;
    cpp_int c = generateRandomCppInt(1 , n-1);
    cpp_int d = 1;

    while( d == 1){
        a = (a * a + c) % n;
        b = (b * b + c) % n;
        b = (b * b + c) % n;
        d = gcd(abs(a - b) , n);
    }

    return d;

}


void factorize(cpp_int n){

    if(n <= 1) return;

    std::ifstream inputFile("prime-numbers.csv");
    std::string a_string;
    while(getline(inputFile , a_string)){

        cpp_int a(a_string);

        while(n % a == 0){
            std::cout<<a<<", ";
            n /= a;
        }

    }

    while(n>1){

        cpp_int factor = pollard_rho(n);
        
        while(n % factor == 0){
            std::cout<<factor<<", ";
            n /= factor;
        }
    }
    
}

int main(){
    std::string n_string;
    std::cin>>n_string;

    cpp_int n(n_string);
    factorize(n); 
}