#include <stdio.h>

#define LOWER 0 /* lower limit odf table */
#define UPPER 30 /* upper limit */
#define STEP 2 /* step size */

float celsiusToFahrenheit(int celsius);

/* print Fahrenheit-Celsius table for fahr = 0, 20, ..., 300; floating-point version */

int main()
{
    float celsius;
    for (celsius = LOWER; celsius < UPPER; celsius = celsius + STEP)
    {
        printf("%3.0f %6.1f\n", celsius, celsiusToFahrenheit(celsius));
    }
}

float celsiusToFahrenheit(int celsius)
{
    return (celsius/(5.0/9.0)+32.0);
}