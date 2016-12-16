#include<iostream>
using namespace std;

void GeneratePosition(int n, int *ran) {
    
    int i = 0, flag = 0;
    
    while (i < n) {
        
        ran[i] = rand() % n;
        
        /*for (int j = 0; j < i; j++) {
            
            if(ran[i] == ran[j]) {
                flag = 1;
            }
        }
        
        if(flag == 1) {
            flag = 0;
            continue;
        }
        */
        cout<<"ran is : "<<ran[i]<<"\n"; 
        
        i++;
    }
}

int fitness(int *ran, int n) {
    
    int fitness = 0, present, present_x, present_y, next, next_x, next_y, count;
    
    for(int i = 0; i < n; i++) {

    count = 1;

        for(int j = i+1; j < n; j++) {

            present = ran[i];
            present_x = ran[i];
            present_y = i;

            next = ran[j];
            next_x = ran[j];
            next_y = j;

            if(present_x + count == next_x && present_y + count == next_y) 
                fitness++;

            else if(present_x + present_y == next_x + next_y)
                    fitness++;

            else if(present_x == next_x)
                    fitness++;

            count++;
        }
    }
    return fitness;
}

int main() {
    
    srand (time(NULL));
    
    int n, i = 0, fit_orig, AR_Flag = 0, initial_position, i_zero, zero_flag = 0, i_min, min_flag = 0, j = 0, opt = 0, turn = 0, count = 0;
    
    
    
    cout<<"Enter n for number of queens : \n";
    cin>>n;
    
    int all_fit[n], all_fit_min = n * n, global_fit = n * n;
    
    int *positions = new int[n];
    
    while(turn < 100) {
        
        GeneratePosition(n, positions);
        
        j = 0;
        count = 0;
    
        while(j < n)
        {
            initial_position = positions[j];

            if(count == 0) {
                fit_orig = fitness(positions, n);
                cout<<"Starting Fitness is : "<<fit_orig<<"\n";
                all_fit_min = fit_orig;
            }

            for(int i = 0; i < n; i++)
            {
                positions[j] = i;

                all_fit[i] = fitness(positions, n);

                cout<<"j is : "<<j<<" i is : "<<i<<" fitness is : "<<all_fit[i]<<"\n";

                if(all_fit[i] == 0){
                    i_zero = i;
                    zero_flag = 1;
                    break;
                }

                if(all_fit[i] < all_fit_min) {
                    i_min = i;
                    all_fit_min = all_fit[i];
                    min_flag = 1;
                }
            }

            cout<<j<<"th column min fitness is : "<<all_fit_min<<"\n";

            if(zero_flag == 1) {
                cout<<"Zero Fitness Caught \n";
                opt++;
                all_fit_min = 0;
                zero_flag = 0;
                positions[j] = i_zero;
                break;
            }

            if(min_flag == 1)
            {
                cout<<"Inter min caught in "<<j<<"\n";
                min_flag = 0;
                positions[j] = i_min;

                if(j != 0)
                    AR_Flag = 1;
            }
            else
                positions[j] = initial_position;

            if(j == n - 1 && AR_Flag == 1) {
                cout<<"Flagged \n";
                j = -1;
                AR_Flag = 0;
            }
            
            count++;

            j++;
        }
        
        if(global_fit > all_fit_min)
            global_fit = all_fit_min;
        
        turn++;
    }
    
    cout<<"Min fitness is : "<<global_fit<<"\n";
    cout<<"Number of optimizations are : "<<opt<<"\n";
}