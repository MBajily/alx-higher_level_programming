#include "Python.h"
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	wprintf(L"[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		wprintf(L"  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		wprintf(L"  type: compact ascii\n");
	}
	else
	{
		wprintf(L"  type: compact unicode object\n");
	}
	wprintf(L"  length: %lu\n", length);
	wprintf(L"  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
