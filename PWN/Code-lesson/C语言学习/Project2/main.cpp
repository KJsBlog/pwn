#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
    char s[] = "c61b68366edeb7bdce3c6820314b7498";
	char v3; 
	int i; 
	int j;
    char t;
    cout << s;
    for (i = 0; i < strlen(s); ++i)
    {
        if ((i & 1) != 0)
            v3 = 1;
        else
            v3 = -1;
        t = s[i] + v3;
        cout << t<<endl;
    }
}