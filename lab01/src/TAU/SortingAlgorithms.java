package TAU;

import java.util.Random;
import java.util.Scanner;


public class SortingAlgorithms
{	
	public static void main(String[] args)
	{
		char option='\0';
		Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[50];
		
        NewRandomTable(numbers);

		System.out.println("----------------------------------------------------------");
		
		do{
           
			System.out.println("============================");
            System.out.println("Wybierz algorytm sortowania:");
            System.out.println("============================");
            System.out.println("1. Sortowanie przez wybieranie");
            System.out.println("2. BubbleSort");
            option = scanner.next().charAt(0);
            System.out.println("\n");

            switch (option){
                case '1':
                	
                	System.out.println("Sortowanie przez wybieranie wynik: ");
                	SelectionSort(numbers);
                	System.out.println("============================");
                	ShowTable(numbers);
                	System.out.println("============================");
                	NewRandomTable(numbers);
                	System.out.println("============================");
                    break;

                case '2':
                	System.out.println("BubbleSort wynik: ");
                	BubbleSort(numbers);
                	System.out.println("============================");
                	ShowTable(numbers);
                	System.out.println("============================");
                	NewRandomTable(numbers);
                	System.out.println("============================");
                    break;

                case '3':
                	throw new IllegalArgumentException();
                	
                	
                default:
                    System.out.println("Wybierz Algorytm!");
            }
        }while(option != '5');
		
		
	}
	// Sorotwanie przez Wybieranie
	public static void SelectionSort(int[] numbers) 
	{
		int lenght = numbers.length;
		long start = System.nanoTime();
		for(int i = 0; i < lenght -1; i++) 
		{
			int minIndex = i;
			
			for(int j = i + 1; j < lenght; j++)
			{
				if(numbers[j] < numbers[minIndex])
				{
					minIndex = j;
				}
			}
			
			int tmp = numbers[minIndex];
			numbers[minIndex] = numbers[i];
			numbers[i] = tmp;
		}
		long end = System.nanoTime();
		double total = (double)(end - start)/1000000;
		System.out.println("Total time = " + total + " ms");
	}
	//BubbleSort
	public static void BubbleSort(int[] numbers) 
	{
		long start = System.nanoTime();
		
		int lenght = numbers.length;
		for(int i = 0; i < lenght -1; i++) 
		{
			for(int j = 0; j < lenght-i-1; j++) 
			{
				if(numbers[j] > numbers[j+1]) 
				{
					int tmp = numbers[j];
					numbers[j] = numbers[j+1];
					numbers[j+1] = tmp;
				}
			}
		}
		long end = System.nanoTime();
		double total = (double)(end - start)/1000000;
		System.out.println("Total time = " + total + " ms");
	}
	
	public static void NewRandomTable(int[] numbers) {
		
		Random rnd = new Random();
		for(int i = 0; i < numbers.length; i++) 
		{
			numbers[i] = rnd.nextInt(1000);
		}
		System.out.println("Wylosowana Tablica: ");
		for(int i = 0; i < numbers.length; i++) 
		{
			System.out.println("index = " + i + "  |  " + "value = " + numbers[i]);
		}
		
	}
	
	public static void ShowTable(int[] numbers) {
		
		System.out.println("Po Sorotwaniu: ");
		for(int i = 0; i < numbers.length; i++) 
		{
			System.out.println("index = " + i + "  |  " + "value = " + numbers[i]);
		}
	}
}
