#include <stdio.h>
#include<unistd.h>
#define LEN 500  // max length of expression


typedef struct{
    char type;
    union{
        char b;
        long int num;
        double numd;};
} block;

block buff[LEN];
int i=0;

int solve_rec(int s, int e);

void del_space(int v){
    for(int j=v; j<i-1;j++){
        buff[j] = buff[j+1];
    }
    i--;
}

int solve(){

    for(int j=0; j<i;j++){
        if(buff[j].b >= '0' && buff[j].b <= '9'){
            buff[j].type = 'd';
            buff[j].num = buff[j].b - '0';
        }
        
    }

    for(int j=0; j<i;j++){
        if(buff[j].type == 'c'){
            if(buff[j].b == ' '){
                del_space(j); j--;
            }
        }
        if(j + 1 < i){
            if(buff[j].type == 'd' && buff[j+1].type == 'd'){
                buff[j].num = buff[j].num * 10 + buff[j+1].num;
                buff[j+1].type = 'c';buff[j+1].b = ' ';
                //i--;
            }
        }
    }

    return solve_rec(0, i);
    
}

void print_arr(int s, int e){
    printf("\n---\n");
    for(int j=s; j<e; j++){
        if(buff[j].type == 'c'){putchar(buff[j].b);}
        else{printf("%ld", buff[j].num);}
    }
    putchar('\n');
}

int solve_rec(int s, int e){
    if(e-s == 1 || i == 1){return buff[s].num;}

    for(int j=s; j<e; j++){
                if(buff[j].b == '('){
                int sc_cnt = 1;
                int w=j+1;
                while(w>e||sc_cnt>0){
                    if(buff[w].b == '('){sc_cnt++;}
                    else if(buff[w].b == ')'){sc_cnt--;}

                    w++;
                }
                w--;
                
                buff[j].type = 'd';
                buff[j].num = solve_rec(j+1, w);
                e -= (w - j);

                del_space(j+1);del_space(j+1);

            }
    }


    for(int j=s; j<e;j++){
        if(buff[j].type == 'c'){

            if(j + 1 < i){

                if((buff[j].b == '*') && (buff[j-1].type == 'd') && (buff[j+1].type == 'd')){
                    buff[j-1].num *= buff[j+1].num;
                    del_space(j); del_space(j); j=s; e -= 2;
                }
                if((buff[j].b == '/') && (buff[j-1].type == 'd') && (buff[j+1].type == 'd')){
                    buff[j-1].num /= buff[j+1].num;
                    del_space(j); del_space(j); j=s; e -= 2;
                }
            }
        }
    }
        for(int j=s; j<e;j++){
        if(buff[j].type == 'c'){
            if(j + 1 < i){
                if((buff[j].b == '+') && (buff[j-1].type == 'd') && (buff[j+1].type == 'd')){
                    buff[j-1].num += buff[j+1].num;
                    del_space(j); del_space(j); j=s; e -= 2;
                }
                if((buff[j].b == '-') && (buff[j-1].type == 'd') && (buff[j+1].type == 'd')){
                    buff[j-1].num -= buff[j+1].num;
                    del_space(j); del_space(j); j=s; e -= 2;
                }
        }}}
    return solve_rec(s, e);
}

int main()
{
    char bu;
    while((bu = getchar()) != '\n'){buff[i].type = 'c';buff[i].b = bu; i++;}
    int ans = solve();
    printf("%d\n", ans);
    
    return 0;
}
