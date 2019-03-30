#include <iostream>
#include <string>

int i;
int a;
int apples;
int pies;
int chef;

int main(void) {
  
 start:
  std::cout << apples << " Apples" << std::endl;
  std::cout << pies << " Pies" << std::endl;
  std::cin >> a;
  
  if ( a==1 ) {
    apples = apples + 1;
    goto start;
  }
  
  if ( a==2 ) {
    if ( apples>=30 ) {
      apples = apples - 30;
      pies = pies + 1;
      goto start;
    } else {
      std::cout << "You dont have enough apples" << std::endl;
      goto start;
    }
  }
  
  if ( a==3 ) {
    if ( apples>=100 ) {
      apples = apples - 100;
      chef = chef + 1;
      goto start;
    } else {
      std::cout << "You dont have enough apples" << std::endl;
      goto start;
    }
  }
  
  
 start1:  
  if ( chef==1 ) {
    for ( int i=0; i<10; ++i ) {
      if ( i==10 ) {
	pies = pies + 1;
	i=i-10;
      }
      goto start1;
    }
  }
  
  return 0;
}
