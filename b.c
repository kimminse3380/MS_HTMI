#include <stdio.h>
int main() {
    int a[101];
	int n=0,m=0, cnt=0;
	scanf("%d", &n);
	for(int i=0;i<=n;i++){
		scanf("%d",&m);
		a[i]=m;
	}
    for (int i =0; i<=n; i++){
        for(int j=i+1; i<=n; j++){
            if(a[i]>a[j]){
                cnt++;
            }
        }
    }
    printf("%d", cnt);
	return 0;
}
