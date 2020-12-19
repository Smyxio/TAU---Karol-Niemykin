package TAU;

import static org.junit.Assert.*;
import org.junit.Test;
/*
 * Trzy wybrane assercje:
 * - assertSame
 * - assertArrayEquals
 * - assertEquals
 */
class Tests1 {
	
	private SortingAlgorithms sort = new SortingAlgorithms();

	@Test
    public void NewTableCheck() {
       int[] values = { 1,2,3,4,5};
       
       sort.NewRandomTable(values);
       
       assertSame(4, values.length);
	}
	@Test
	public void ShowTableCheck() {
		int[] values = { 123,412,62,12,124};
		
		sort.ShowTable(values);
	}
	
	@Test
    public void BubbleSortCheck() {
        int[] values = { 9, -3, 5, 0, 1};
        int[] expectedOrder = { -3, 0, 1, 5, 9};
 
        sort.BubbleSort(values);
        assertArrayEquals(expectedOrder, values);
	}
	@Test
    public void SelectionSortCheck() {
        int[] values = { 15, -22, 3, 0, 1};
        int[] expectedOrder = { -22, 0, 1, 3, 15};
        
        sort.SelectionSort(values);      
        assertEquals(expectedOrder, values);
	}
	@Test
    public void InsertionSortCheck() {
        int[] values = { 50, -10, 235, 643, 0};
        int[] expectedOrder = { -10, 0, 50, 235, 643};
 
        sort.InsertionSort(values);
        assertArrayEquals(expectedOrder, values);
	}
	
	@Test
    public void SelectionSortEmptyArray() {
        int[] values = {};
        //Should do nothing
        sort.SelectionSort(values);      
       
	}
	
	@Test
	 public void BubbleSortEmptyArray() {
        int[] values = {};
        //Should do nothing
        sort.BubbleSort(values);      
       
	}
	
	@Test
	public void InsertionSortEmptyArray() {
		int[] values = {};
        //Should do nothing
        sort.InsertionSort(values); 
	}
	
	@Test
    public void SelectionSortOneElementArray() {
		int[] values = {10};
		 
	    sort.SelectionSort(values);
	    assertArrayEquals(new int[] {10}, values);
    }
	
	@Test
    public void BubbleSortOneElementArray() {
		int[] values = {20};
		 
	    sort.BubbleSort(values);
	    assertArrayEquals(new int[] {20}, values);
    }
	
	@Test
    public void InsertionSortOneElementArray() {
		int[] values = {30};
		 
	    sort.InsertionSort(values);
	    assertArrayEquals(new int[] {30}, values);
    }
}