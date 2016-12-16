#include<iostream>
using namespace std;

#define _USE_MATH_DEFINES // for C++
#include <cmath>
#include <ctime>

double ackley(double x, double y) {
    
    double t1, t2, res;
    
    t1 = -20 * (exp(-0.2*(sqrt(0.5 * (x*x + y*y)))));
    t2 = exp(0.5 * (cos(2*M_PI*x) + cos(2*M_PI*y)));
    
    res = t1 - t2;
    
    return res;
}

double RandomNumber(double Min, double Max)
{
    return ((double(rand()) / double(RAND_MAX)) * (Max - Min)) + Min;
}

int main() {
    
    srand ( time(NULL) );
    
    double x = 0, y = 0, x_new, y_new, res[10];
    
    int i = 0, j = 0;    
    
    
    
    while(j < 100) {
        
        x = RandomNumber(-5.0, 5.0);
        y = RandomNumber(-5.0, 5.0);
        
        //cout<<"Initial x is : "<<x<<"\n";
        //cout<<"Initial y is : "<<y<<"\n";
        
        i = 0;
        
        while(i < 100) {
        
            res[i] = ackley(x, y);

            if(res[i] > res[i-1]) {
                i = i-1;
                break;
            }

            //cout<<"res is : "<<res[i]<<"\n";

            x_new = x + ((((float)rand() / RAND_MAX) - 0.5) * 0.1); 
            while(x_new > 5.0 || x_new < -5.0) {
                x_new = x + ((((float)rand() / RAND_MAX) - 0.5) * 0.1);   
            }

            y_new = y + ((((float)rand() / RAND_MAX) - 0.5) * 0.1);  
            while(y_new > 5.0 || y_new < -5.0) {
                y_new = y + ((((float)rand() / RAND_MAX) - 0.5) * 0.1);   
            }

            //cout<<"x_new is : "<<x_new<<"\n";
            //cout<<"y_new is : "<<y_new<<"\n";

            x = x_new;
            y = y_new;

            i++;
        }
        
        //cout<<"j is "<<j<<" res is "<<res[i]<<" i is "<<i<<"\n";
        
        cout<<j<<"\t"<<res[i]<<"\n";
        
        j++;
        
    }
    
      
}