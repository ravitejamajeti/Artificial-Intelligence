#include<iostream>
using namespace std;

void GeneratePosition(int n, int *ran) {
    
    int i = 0, flag = 0;
    
    while (i < n) {
        
        ran[i] = rand() % n;
        
        for (int j = 0; j < i; j++) {
            
            if(ran[i] == ran[j]) {
                flag = 1;
            }
        }
        
        if(flag == 1) {
            flag = 0;
            continue;
        }
        
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
    
    int n, niter, count, i = 0, fit_orig, fit_up, fit_down, fit_up_temp, fit_down_temp, fit_new, position, optimized = 0, AR_Flag = 0, num_optimizations = 0, run = 0, fit_min;
    
    cout<<"Enter n for number of queens : \n";
    cin>>n;
    
    fit_min = n*n;
    
    cout<<"Enter number of iterations : \n";
    cin>>niter;
    
    char move;
    
    int *positions = new int[n];
    
    
    /*
    GeneratePosition(n, positions);
    
    positions[0] = 1;
    positions[1] = 4;
    positions[2] = 7;
    positions[3] = 2;
    positions[4] = 0;
    positions[5] = 3;
    positions[6] = 6;
    positions[7] = 5;*/
    
    while(run < niter) {
        
        cout<<"run is "<<run<<"\n";
        
        GeneratePosition(n, positions);
        
        for(int i = 0; i < n; i++) {
        cout<<"position is "<<positions[i]<<","<<i<<"\n";
        }
        
        fit_orig = fitness(positions, n);
        
        cout<<"fitness is : "<<fit_orig<<"\n";
        
        i = 0;
        
        optimized = 0;
        AR_Flag = 0;
        
    
        while(i < n) {

            cout<<"##############################\n";
            cout<<"Looping for "<<positions[i]<<"\n";
            cout<<"Orig Fitness is "<<fit_orig<<"\n";


            if(positions[i] < n - 1) {
                cout<<"Calculating down \n"; 
                position = positions[i];
                positions[i] = positions[i] + 1;
                fit_down = fitness(positions, n);
                positions[i] = position;
            }

            if(positions[i] == n - 1) {
                fit_down = n * n;
            }

            if(positions[i] > 0) {
                cout<<"Calculating Up \n"; 
                position = positions[i];
                positions[i] = positions[i] - 1;
                fit_up = fitness(positions, n);
                positions[i] = position;
            }

            if(positions[i] == 0) {
                cout<<"coming to 64 \n";
                fit_up = n * n;
            }

            if(fit_down < fit_orig || fit_up < fit_orig) {

                cout<<"Came inside first if \n";

                cout<<"fit up is "<<fit_up<<"\n";
                cout<<"fit down is "<<fit_down<<"\n";

                if(fit_up == 0 || fit_down == 0) {
                    move = 'n';
                    optimized = 1;

                    if(fit_up == 0)
                        positions[i] = positions[i] - 1;
                    if(fit_down == 0)
                        positions[i] = positions[i] + 1;
                }
                else if(fit_down < fit_up) {
                    move = 'd';
                }
                else if(fit_up < fit_down) {
                    move = 'u';
                }
                else
                    move = 'u';
            }
            else if(fit_up == fit_orig || fit_down == fit_orig) {
                
                if(fit_up == fit_orig && fit_down == fit_orig) {
                    
                    if(positions[i] - 1 > 0 ) {
                        position = positions[i];
                        positions[i] = positions[i] - 2;
                        fit_up_temp = fitness(positions, n);

                        positions[i] = position;
                    }
                    else
                        fit_up_temp = n*n;
                    
                    if(positions[i] + 1 < n - 1) {
                        position = positions[i];
                        positions[i] = positions[i] + 2;
                        fit_down_temp = fitness(positions, n);

                        positions[i] = position;
                    }
                    else
                        fit_down_temp = n*n;
                    
                    if(fit_down_temp < fit_up_temp) {
                        if(fit_down_temp < fit_orig)
                            move = 'd';
                    }
                    else if(fit_up_temp < fit_down_temp) {
                        if(fit_up_temp < fit_orig)
                            move = 'u';
                    }
                    else
                        move = 'n';
                    
                }
                else if(fit_up == fit_orig) {
                    
                    if(positions[i] - 1 > 0) {
                        position = positions[i];
                        positions[i] = positions[i] - 2;
                        fit_up_temp = fitness(positions, n);

                        positions[i] = position;
                    }
                    else
                        fit_up_temp = n*n;
                    
                    if(fit_up_temp < fit_orig)
                        move = 'u';
                    else
                        move = 'n';
                }
                else if(fit_down == fit_orig) {
                    
                    if(positions[i] + 1 < n - 1) {
                        position = positions[i];
                        positions[i] = positions[i] + 2;
                        fit_down_temp = fitness(positions, n);

                        positions[i] = position;
                    }
                    else
                        fit_down_temp = n*n;
                    
                    if(fit_down_temp < fit_orig)
                        move = 'd';
                    else
                        move = 'n';
                }
            }
            else {
                cout<<"Came inside first else \n";
                cout<<"fit up is "<<fit_up<<"\n";
                cout<<"fit down is "<<fit_down<<"\n";
                move = 'n';
            }

            if(move == 'd') {

                if(i != 0)
                    AR_Flag = 1;

                positions[i] = positions[i] + 1;
                fit_orig = fit_down;

                while(1) {

                    position = positions[i];

                    if(positions[i] + 1 > n - 1)
                        break;
                    else {  
                        positions[i] = positions[i] + 1;
                        cout<<"Updating position : "<<positions[i]<<"\n";
                    }

                    fit_new = fitness(positions, n);

                    cout<<"fit_new is "<<fit_new<<"\n";

                    if(fit_new == 0) {
                        optimized = 1;
                        break;
                    }
                    else if(fit_new == fit_down) {
                        if(positions[i] < n - 1) {
                            positions[i] = positions[i] + 1;
                            fit_down_temp = fitness(positions, n);
                            
                            if(fit_down_temp < fit_new)
                                positions[i] = positions[i] - 1;
                            else {
                                fit_orig = fit_down;
                                break;
                            }
                        }
                    }
                    else if(fit_new > fit_down) {
                        fit_orig = fit_down;
                        positions[i] = position;
                        break;
                    }
                    else if(positions[i] == n - 1) {
                        fit_orig = fit_new;
                        AR_Flag = 1;
                        break;
                    }
                    else {
                        AR_Flag = 1;
                        fit_down = fit_new;
                    }

                    cout<<"Looping Down \n";
                }

            }
            else if(move == 'u') {

                if(i != 0)
                    AR_Flag = 1;

                positions[i] = positions[i] - 1;
                fit_orig = fit_up;

                while(1) {

                    position = positions[i];

                    if(positions[i] - 1 < 0)
                        break;
                    else
                        positions[i] = positions[i] - 1;

                    fit_new = fitness(positions, n);

                    if(fit_new == 0) {
                        optimized = 1;
                        break;
                    }
                    else if(fit_new == fit_up) {
                        if(positions[i] > 0) {
                            positions[i] = positions[i] - 1;
                            fit_up_temp = fitness(positions, n);
                            
                            if(fit_up_temp < fit_new)
                                positions[i] = positions[i] + 1;
                            else {
                                fit_orig = fit_up;
                                break;
                            }
                        }
                    }
                    else if(fit_new > fit_up) {
                        fit_orig = fit_up;
                        positions[i] = position;
                        break;
                    }
                    else if(positions[i] == 0) {
                        fit_orig = fit_new;
                        AR_Flag = 1;
                        break;
                    }
                    else {
                        fit_up = fit_new;
                        AR_Flag = 1;
                    }

                    cout<<"Looping Up \n";
                }
            }

            if(optimized == 1) {
                cout<<"Zero Fitness Caught!!!"<<"\n";
                fit_orig = 0;
                num_optimizations++;
                for(int i = 0; i < n; i++) {
                    cout<<"positions for zero fitness "<<positions[i]<<","<<i<<"\n";
                }
                break;    
            }

            for(int i = 0; i < n; i++) {
            cout<<"Updated position is "<<positions[i]<<","<<i<<"\n";
            }

            if(i == n - 1 && AR_Flag == 1) {
                i=0;
                AR_Flag = 0;
                cout<<"Flagged \n";
            }
            else
                i++;
        }
        
        cout<<"Run "<<run<<"'s fitness is : "<<fit_orig<<"\n";
        if(fit_orig < fit_min)
            fit_min = fit_orig;
            
        run++;
    }
    
    cout<<"num_optimizations are : "<<num_optimizations<<"\n";
    cout<<"Total Minimum fitness found is : "<<fit_min
        <<"\n";
}