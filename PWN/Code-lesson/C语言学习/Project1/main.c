#include<stdio.h>
void count() {
	int sum = 0;
	float kl, price = 0;
	int time;
	printf("Input distance and time：\n");
	scanf_s("%f,%d", &kl, &time);
	if (kl >= 3.0) {
		price += 10.0;
		if (kl >= 10.0)
			price += (7.0) * 2.0 + (kl - 10.0) * 3.0;
		else
			price += (kl - 3.0) * 2.0;
	}
	else
		price = 10.0;
	if (time >= 5)
		price += time / 5 * 2;
	printf("fee = %.0f\n", price);
	sum = (int)(price + 0.5);
	price = sum * 1.0;
	printf("fee = %.0f\n", price);
}
int main() 
{
	count();
	return 0;
}