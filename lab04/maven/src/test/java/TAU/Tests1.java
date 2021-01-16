package TAU;

import static org.junit.Assert.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.mockito.BDDMockito.*;

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
	
	
	private int a, b;
	
	@Test
	public void example() {
		SortingAlgorithms Example = new Example();
		a = Example.a();
		assertEquals(0,a);
	}
	
	@Test
	public void example2() {
		SortingAlgorithms Example = mock(SortingAlgorithms.class);
		b = Example.b();
		assertEquals(0,b);
	}
	
	@Test
	public void example2() {
		SortingAlgorithms Example = mock(SortingAlgorithms.class);
		when(Example.b()).thenReturn(2);
		b = Example.b();
		assertEquals(0,b);
	}
	
	@Test
	public void example4() {
		SortingAlgorithms Example = new Example();
		c = Example.c();
		assertEquals("stringTest",c);
	}
	
	@Test
	public void example5() {
		SortingAlgorithms Example = mock(SortingAlgorithms.class);
		given(Example.d().thenReturn("stringTesttwo"));
		d = Example.d();
		assertEquals("stringTesttwo",d);
	}
	
	
}

