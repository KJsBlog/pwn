//#include<bits/stdc++.h>
//using namespace std;
//bool a[12];//表示1~12号位是否使用过
//int st[12];//表示1~12号位的当前状态
//int n;//表示一共有多少个数
//int shu;//表示到了第几个数
//void dfs(int shu)
//{
//	if (shu == n)			 //满足条件就输出
//	{
//		for (int rou = 0; rou <n; rou++)
//			printf("%d  ",st[rou]);
//		printf("\n");
//		return;
//	}
//	for (int i= 1; i <= n; i++)
//	{
//		if (a[i] == 0)			//表示i这个数还没用过
//		{
//			st[shu] = i;		//此是把当前状态存储在st数组里
//			a[i] = 1;			//表示i这个数已经用了
//			dfs(shu + 1);		//重头戏：递归，意思是第shu这个位置的数已经确认了，
//			                    //接着向shu+1这个位置的数寻找，此时递归到shu+1层的时候。for循环
//								//和if循环一个个由1到n里边找还没用过的数（既a[shu+1]为0的值）
//			a[i] = 0;			//此时作为递归完shu+1返回至递归层shu的递归层，这时相当于没有选择i这个
//								//数进行插入，所以把它的a[i]值赋值为0；
//		}
//	}
//}
//int main()
//{
//	scanf_s("%d",&n);
//	dfs(0);
//}