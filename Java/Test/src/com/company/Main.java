package com.company;

public class Main {
    public static void insertionSort2(int n, int[] arr) {
        for(int i = 0;i<arr.length-1;i++){
            int k = arr[i+1];
            for(int j=i;j>-1;j--){
                if(arr[j] > k){
                    arr[j+1] = arr[j];
                    if(arr[j] > k&&j==0){
                        arr[j+1]=arr[j];
                        arr[0]=k;
                    }
                }
                else {
                    arr[j+1]=k;
                    break;
                }
            }
            in(arr);
        }
    }
    public static void in(int []arr){
        for(int i = 0 ;i< arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.print("\n");
    }
    public static void main(String[] args) {
	// write your code here
        int[] arr = {1,9,0,2,4,3};
        insertionSort2(arr.length,arr);
    }
}
