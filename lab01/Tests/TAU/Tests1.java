package TAU;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
/*
 * Trzy wybrane assercje:
 * - assertSame
 * - assertArrayEquals
 * - assertEquals
 */
class Tests1 {
	
	private SortingAlgorithms sort = new SortingAlgorithms();

	@Test
    public void newTable() {
       int[] values = { 1,2,3,4,5};
       
       sort.NewRandomTable(values);
       
       assertSame(4, values.length);
	}
	@Test
    public void bubbleSortCheck() {
        int[] values = { 9, -3, 5, 0, 1};
        int[] expectedOrder = { -3, 0, 1, 5, 9};
 
        sort.BubbleSort(values);
        assertArrayEquals(expectedOrder, values);
	}
	
	@Test
    public void selectionSortCheck() {
        int[] values = { 15, -22, 3, 0, 1};
        int[] expectedOrder = { -22, 0, 1, 3, 15};
        
        sort.SelectionSort(values);      
        assertEquals(expectedOrder, values);
	}
	
	@Test
    public void shouldDoNothingWithEmptyArray() {
        int[] values = {};
        
        sort.SelectionSort(values);      
       
	}
	
	@Test
    public void shouldDoNothingWithOneElementArray() {
        int[] values = {42};
 
        sort.BubbleSort(values);
        assertArrayEquals(new int[] {42}, values);
    }
	
	

}
