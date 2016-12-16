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
        //cout<<"ran is : "<<ran[i]<<"\n"; 
        
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
    
    int n, i = 0, fit_orig, AR_Flag = 0, initial_position, i_zero, zero_flag = 0, i_min, min_flag = 0, j = 0, opt = 0, turn = 0, j_min, fit_min, position, fit_now;
    
    
    
    cout<<"Enter n for number of queens : \n";
    cin>>n;
    
    int all_fit[n], global_fit = n * n;
    
    int *positions = new int[n];
    
    while(turn < 100) {
        
        GeneratePosition(n, positions);
        
        if(turn < 10) {
            cout<<"\nRun Number is - "<<turn<<"\n";
            
            cout<<"\nInitial Positions are \n";
            
            for(int row = 0; row < n; row++){
                for(int column = 0; column < n; column++) {
                    if(positions[column] == row) {
                        cout<<" * ";
                    }
                    else
                        cout<<" . ";
                }
                cout<<"\n";
            }
            
            cout<<"\n";
            for(int pos = 0; pos < n; pos++)
                    cout<<positions[pos]<<" ";
            cout<<"\n";
        }
        
        j = 0;
        
        fit_orig = fitness(positions, n);
        fit_min = fit_orig;
    
        while(j < n)
        {     
            position = positions[j];
            
            for(int i = 0; i < n; i++) {
                positions[j] = i;
                
                fit_now = fitness(positions, n);
                
                if(fit_now == 0){
                    i_zero = i;
                    zero_flag = 1;
                    i_min = i;
                    j_min = j;
                    break;
                }
                
                if(fit_now < fit_min) {
                    fit_min = fit_now;
                    min_flag = 1;
                    i_min = i;
                    j_min = j;
                        
                }      
            }
            
            positions[j] = position;
            
            if(zero_flag == 1) {
                opt++;
                positions[j] = i_zero;
                cout<<"\nZero positions are found as below in run : "<<turn<<"\n \n";
                
                for(int row = 0; row < n; row++){
                    for(int column = 0; column < n; column++) {
                        if(positions[column] == row) {
                            cout<<" * ";
                        }
                        else
                            cout<<" . ";
                    }
                cout<<"\n";
                }
                
                cout<<"\n";
                for(int pos = 0; pos < n; pos++)
                    cout<<positions[pos]<<" ";
                cout<<"\n";
                zero_flag = 0;
                fit_min = 0;
                break;
            }
            
            if(j == n - 1 && min_flag == 1 ){
                positions[j_min] = i_min;
                min_flag = 0;
                j = -1;
            }
            
            j++;
            
        }
        
        if(global_fit > fit_min)
            global_fit = fit_min;
        
        if(turn < 10) {
            cout<<"\nFinal Positions are \n";
            
            for(int row = 0; row < n; row++){
                for(int column = 0; column < n; column++) {
                    if(positions[column] == row) {
                        cout<<" * ";
                    }
                    else
                        cout<<" . ";
                }
                cout<<"\n";
            }
            
            cout<<"\n";
            for(int pos = 0; pos < n; pos++)
                    cout<<positions[pos]<<" ";
            cout<<"\n";
        }
        
        turn++;
    }
    
    cout<<"\nMin fitness on the whole is : "<<global_fit<<"\n";
    cout<<"\nNumber of optimizations are : "<<opt<<"\n\n";
}