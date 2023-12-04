#include <listobject.h>
#include <Python.h>
#include <object.h>


/**
 * print_python_list_info
 *
 * PyObject *p
 */
void print_python_list_info(PyObject *p)
{
	int i;
	long int s = PyList_Size(p);

	PyListObject *ob = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", ob->allocated);
	
	for (i = 0; i < s; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(ob->ob_item[i])->tp_name);
	}
}
