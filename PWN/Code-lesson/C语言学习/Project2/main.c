//#define _CRT_SECURE_NO_WARNINGS
//#include<stdio.h>
//#include<intrin.h>
//int __cdecl main(int argc, const char** argv, const char** envp)
//{
//    char v3; // al
//    int i; // [rsp+0h] [rbp-40h]
//    int j; // [rsp+4h] [rbp-3Ch]
//    FILE *stream; // [rsp+8h] [rbp-38h]
//    char filename[24]; // [rsp+10h] [rbp-30h] BYREF
//    unsigned __int64 v9; // [rsp+28h] [rbp-18h]
//    char t;
//    char s[36] = "c61b68366edeb7bdce3c6820314b7498";
//    char p[1000];
//    char u = "*******************************************";
//    for (i = 0; i < strlen(s); ++i)
//    {
//        if ((i & 1) != 0)
//            v3 = 1;
//        else
//            v3 = -1;
//        *(&t + i + 10) = s[i] + v3;
//    }
//    strcpy(filename, "/tmp/flag.txt");
//    stream = fopen(filename, "w");
//    fprintf(stream, "%s\n", u);
//    for (j = 0; j < strlen(&t); ++j)
//    {
//        fseek(stream, p[j], 0);
//        fputc(*(&t + p[j]), stream);
//        fseek(stream, 0LL, 0);
//        fprintf(stream, "%s\n", u);
//    }
//    fopen(stream,"r");
//    return 0;
//}