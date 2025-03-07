#include<stdio.h>
int main()
{
    int table,num2,i;
    printf("enter a no to find the table:");
    scanf("%d",&table);
    for(i=1;i<=10;i++)
    {
    num2=table*i;
    printf("%d X %02d = %03d\n",table,i,num2);
    }
}