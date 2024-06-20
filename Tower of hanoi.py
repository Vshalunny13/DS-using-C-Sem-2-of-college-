#include<stdio.h>
#include<conio.h>
void moveDisks(int numDisks, char fromPeg, char toPeg, char auxPeg) {
    if (numDisks == 1) {
        printf("Move disk 1 from %c to %c\n", fromPeg, toPeg);
        return;
    }
    moveDisks(numDisks - 1, fromPeg, auxPeg, toPeg);
    printf("Move disk %d from %c to %c\n", numDisks, fromPeg, toPeg);
    moveDisks(numDisks - 1, auxPeg, toPeg, fromPeg);
}

int main() {
    int n;
    printf("Enter the number of disks: ");
    scanf("%d", &n);
    moveDisks(n, 'A', 'C', 'B');
    return 0;
}