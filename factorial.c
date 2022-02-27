#include <stdio.h>
int factorial(int n);

int main() {
    int number, result;

    printf("Enter a number to find its factorial: ");
    //
    scanf("%i", &number);

    result = factorial(number);

    printf("Factorial %i = %i", number, result);
    return 0;
}

int factorial(int i) {
    if (i == 0)
        return 1;
    else
        // factorial function calls itself
        return i * factorial(i-1); 
}
