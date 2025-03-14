#include<stdio.h>
int main()
{
    int weekday;
    puts("enter a weekday number:");
    scanf("%d",&weekday);
    switch(weekday)
    {
        case 1 : puts("Monday");
        break;
        case 2 : puts("tuesday");
        break;
        case 3 : puts("wednesday");
        break;
        case 4 : puts("thursday");
        break;
        case 5 : puts("friday");
        break;
        case 6 : puts("saturday");
        break;
        case 7 : puts("sunday");
        break;
        default: puts("SORRY! weekday not found");

    }
}