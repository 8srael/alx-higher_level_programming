#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Print some basic info about Python lists
 *
 * @p: PyObject
 *
 */

void print_python_list_info(PyObject *p)
{
	PyObject item;
	PyListObject *list = (PyListObject *)p;
	int j, size, alloc;

	size = Py_SIZE(p);
	
	alloc = list->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	
	for (j = 0; j < size; j++)
	{
		item = PyList_GetItem(p, j);
		printf("Element %d: %s\n", j, Py_TYPE(item)->tp_name);
	}
}	
