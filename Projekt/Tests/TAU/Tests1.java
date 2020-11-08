package TAU;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Tests1 {
	
	private SortingAlgorithms sort = new SortingAlgorithms();
	
	@Test
    public void shouldDoNothingWithEmptyArray() {
        int[] values = {};
 
        sort.BubbleSort(values);
    }
	
	@Test
    public void shouldDoNothingWithOneElementArray() {
        int[] values = {42};
 
        sort.BubbleSort(values);
        assertArrayEquals(new int[] {42}, values);
    }
	
	@Test
    public void shouldSortValues() {
        int[] values = { 9, -3, 5, 0, 1};
        int[] expectedOrder = { -3, 0, 1, 5, 9};
 
        sort.BubbleSort(values);
        assertArrayEquals(expectedOrder, values);
    }

}
