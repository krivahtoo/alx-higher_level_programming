#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    int i = 0;
    PyObject *ptr;
    PyTypeObject *type;
    Py_ssize_t len = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", len);
    printf("[*] Allocated = %ld\n", Py_SIZE(p));
    while (i < len)
    {
        ptr = PyList_GetItem(p, i);
        type = Py_TYPE(ptr);
        printf("Element %d = %s\n", i, type->tp_name);
        i++;
    }
}
