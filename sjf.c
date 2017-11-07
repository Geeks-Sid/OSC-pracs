#include<stdio.h>
int a[100][6], n;
void sortbyarrival() {
	int i, j, temp1;
	printf("\nInside the sort by burst");
	for (i = 0; i < n; i++)
	{
		for (j = i+1; j < n; j++)
		{
			if (a[i][2] > a[j][2])
			{
				temp1 = a[i][0];
				a[i][0] = a[j][0];
				a[j][0] = temp1;
				temp1 = a[i][1];
				a[i][1] = a[j][1];
				a[j][1] = temp1;
				temp1 = a[i][2];
				a[i][2] = a[j][2];
				a[j][2] = temp1;
			}
		}
	}
}

void processprinter() {
	printf("\nThe processes look as follows :");
	printf("\n      Process ID               ");
	int i;
	for (i = 0; i < n; i++)
	{
		printf("  %d", a[i][0]);
	}
	printf("\n      arrival time of process :");
	for (i = 0; i < n; i++)
	{
		printf("  %d", a[i][1]);
	}
	printf("\n      burst time of process :  ");	
	for (i = 0; i < n; i++)
	{
		printf("  %d", a[i][2]);
	}
	printf("\n completion time of process :  ");	
	for (i = 0; i < n; i++)
	{
		printf("  %d", a[i][3]);
	}
	printf("\nTurn around time of process :  ");
	for (i = 0; i < n; i++)
	{
		printf("  %d", a[i][4]);
	}
	printf("\n    Waiting time of process :  ");
	for (i = 0; i < n; i++)
	{
		printf("  %d", a[i][5]);
	}
}

void initblank() {
	printf("\nInitializing a blank array :");
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < 6; j++)
		{
			a[i][j] = 0;
		}
	}
}

void calcomplete() {
	int i , j, temp1, temp2;
	a[0][3] = a[0][2] + a[0][1];
	for(i = 1;i < n; i++) {
		a[i][3] = a[i-1][3] + a[i][2];
	}
}

void tat() {
	int i, j, temp1 = 0;
	for (i = 0; i < n; i++)
	{
		a[i][4] = a[i][3] - a[i][1];
	}
}

void watcalc() {
	int i, j, temp1 = 0;
	a[0][5] = 0;
	for (i = 1; i < n; i++)
	{
		a[i][5] = a[i][4] - a[i][2];
	}
}

void avgtat() {
	int i, j, temp1 = 0;
	double avg;
	for (i = 0; i < n; i++)
	{
		temp1 += a[i][4];
	}
	avg = temp1 / n;
	printf("\nAverage turn around time is: %lf", avg);
}

void avgwat() {
	int i, j, temp1 = 0;
	double avg;
	for (i = 0; i < n; i++)
	{
		temp1 += a[i][5];
	}
	avg = temp1 / n;
	printf("\nAverage waiting time is: %lf", avg);
}

void main () {
	int i;
	printf("\nEnter the maximum number of processes :");
	scanf("%d", &n);
	initblank();
	processprinter();
	for (i = 0; i < n; i++)
	{
		a[i][0] = i+1;
		printf("\nEnter the start time of process [%d] :", i + 1 );
		scanf(" %d", &a[i][1]);
		printf("\nEnter the burst time of process [%d] :", i + 1 );
		scanf(" %d", &a[i][2]);
	}
	processprinter();
	printf("\n");
	printf("\n----Sorting by burst time----");
	sortbyarrival();
	printf("\n----Sorting has been done------");
	processprinter();
	printf("\n-----Calculating completion time------");
	calcomplete();
	printf("\n----Completion time has been done------");
	processprinter();
	printf("\n-----Calculating Turn around time------");
	tat();
	printf("\n----Turn around time has been done-----");
	processprinter();
	printf("\n-----Calculating Waiting time------");
	watcalc();
	printf("\n----Waiting time has been done-----");
	processprinter();
	printf("\n-----Calculating Average turn around time------");
	avgtat();
	printf("\n----Average turn around time has been done-----");
	printf("\n-----Calculating Average turn around time------");
	avgwat();
	printf("\n----Average turn around time has been done-----\n\n");
}