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

double RandomNumber(double Min, double Max) {

    return ((double(rand()) / double(RAND_MAX)) * (Max - Min)) + Min;
}


int main() {
    
    srand ( time(NULL) );
    
    int np = 10, i = 0, nc = 100, a, b, c, run = 0;
    
    double x1[3 * np], x0[3 * np], F = 0.8, U[2], V[2], CR = 0.1, ran, ackley_u, ackley_i, ackley_min = 100.0;
    
    while(run < 100) {
        ackley_min = 100.0;
        
        cout<<"\nRun number is "<<run<<"\n";
        
        i = 0;
    
    while(i < np) {
    
        x1[i] = RandomNumber(-5.0, 5.0);
        x1[np + i] = RandomNumber(-5.0, 5.0);
        
        i++;
    
    }
    
    cout<<"\n";
    for(int i = 0; i < np; i++) {
        x1[(2 * np) + i] = ackley(x1[i], x1[np + i]);
        cout<<"Initial x,y values are  "<<" -- x is : "<<x1[i]<<" -- y is "<<x1[np + i]<<" -- Its Ackley is : "<<x1[(2 * np) + i]<<"\n";
    }
    
        cout<<"\n";
    for(int k = 0; k < nc; k++) {
        
        memcpy(x0, x1, 3 * np * sizeof(double));
        
        for(int i = 0; i < np; i++) {
            
            do
            {
              a = rand() % np;
            } while (a == i);
                
            do
            {
              b = rand() % np;
            } while (b == i || b == a);
            
            do
            {
              c = rand() % np;
            } while (c == i || c == b || c == a);
            
            //cout<<"i is : "<<i<<" -- a is : "<<a<<" -- b is : "<<b<<" -- c is : "<<c<<"\n";
            
            V[0] = x0[a] + F * (x0[b] - x0[c]);
            V[1] = x0[a + np] + F * (x0[b + np] - x0[c + np]);
            
            ran = (float)rand() / RAND_MAX;
            
            if(ran < CR)
                U[0] = V[0];
            else
                U[0] = x0[i];
            
            ran = (float)rand() / RAND_MAX;
            
            if(ran < CR)
                U[1] = V[1];
            else
                U[1] = x0[i + np];
            
            ackley_u = ackley(U[0], U[1]);
            ackley_i = ackley(x0[i], x0[i + np]);
            
            if(ackley_u < ackley_i) {
                x1[i] = U[0];
                x1[i + np] = U[1];
            }
            else {
                x1[i] = x0[i];
                x1[i + np] = x0[i + np];
            }     
        }
    }
    
    cout<<"\n";
    for(int i = 0; i < np; i++) {
        x1[(2 * np) + i] = ackley(x1[i], x1[np + i]);
        cout<<"Final x,y values are  "<<" -- x is : "<<x1[i]<<" -- y is "<<x1[np + i]<<" -- Its Ackley is : "<<x1[(2 * np) + i]<<"\n";
        if(x1[(2 * np) + i] < ackley_min) {
            ackley_min = x1[(2 * np) + i];
        }
    }
        
    cout<<run<<"\t"<<ackley_min<<"\n";
        
    cout<<"\n";
        run++;
    }
    
    //cout<<"Zero Ackley is "<<ackley(0, 0)<<"\n";
}