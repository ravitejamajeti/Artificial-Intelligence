#include<iostream>
using namespace std;

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
    
    int n = 16;
    
    int *positions = new int[n];
    
    positions[0] = 6;
    positions[1] = 11;
    positions[2] = 7;
    positions[3] = 2;
    positions[4] = 0;
    positions[5] = 12;
    positions[6] = 14;
    positions[7] = 8;
    positions[8] = 10;
    positions[9] = 13;
    positions[10] = 3;
    positions[11] = 5;
    positions[12] = 15;
    positions[13] = 1;
    positions[14] = 9;
    positions[15] = 4;
    
    cout<<"Fitness is : "<<fitness(positions, n)<<"\n";
}