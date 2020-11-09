/*
Program    : ROT 13 Cipher
Created On : 9th November 2020
*/

#include<iostream>
#include<string>
#define shift 13
#define limit 100

void encrypt(std::string str){
  std::cout<<"Encrypted String: "<<std::endl;
  for(int i=0; i<limit && str[i] != '\0';i++){
    char c= str[i];
    if(c >= 65 && c<=90){
      std::cout<< (char)(65 + (((c - 97) + shift )%26));
    }
    else if(c >=97 && c<=122){
      std::cout<< (char)(97 + (((c - 97) + shift )%26));
    }
    else{
      std::cout<<c;
    }
    
  }
  std::cout<<"\n"<<std::endl;
}

int main(){
  std::string in;

  std::cout<<"\nEnter string to encrypt : "<<std::endl;
  getline(std::cin,in);
  encrypt(in);

  return 0;
}
