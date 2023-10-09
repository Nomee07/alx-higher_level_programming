#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %li: %s\n", i, Py_TYPE(item)->tp_name);
	}
}	
