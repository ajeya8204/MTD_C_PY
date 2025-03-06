#include<stdio.h>

int main(){
    int inutnum = 0;
    puts("Enter a no to check if it is Even :");
    scanf("%d",&inutnum);
    if(inutnum%2==0)
        printf("%d is even",inutnum);
    else
        printf("%d is not even",inutnum);
}