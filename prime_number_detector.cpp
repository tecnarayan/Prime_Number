#include <boost/multiprecision/cpp_int.hpp>
#include<bits/stdc++.h>

using namespace boost::multiprecision;

cpp_int x = 1000; // global variable for precision

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
    while(getline(inputFile , a_string) && x--){

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

int main(){

    std::string n_string;
    std::cout<<"number :: ";
    std::cin>>n_string;

    cpp_int n(n_string);

    if(detected_composite(n)) std::cout<<"composite"<<std::endl;
    else std::cout<<"prime"<<std::endl;

}