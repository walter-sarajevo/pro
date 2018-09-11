#include <stdio.h>

int main()
{
  float a = 1.0;
  /* int i = (int &)a; */
  printf("%d\n",(int &)a);
  printf("%x",a);
  return 0;
}
