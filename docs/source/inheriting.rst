Inhering properties
===================

.. _inheriting_props_definition:

What is the inheriting effect ?
--------------------

For some actor nodes is possible to just inherit properties from other ones (following the law of the property inheriting). In different words, in several situations a property that has been already declared can simple be re-used by other actors without re-instancig it again. 

There are two different situations:

#. In the case of the material property of a marble lintel (USM100), the corresponding USV/s 101(reconstruction of the lost part of the lintel) will automatically inherit this property.

#. Other properties are not automatically inherited: in some cases the broken lintel will preserve its original height so that it can be reused by the USV/s 101, in other situations the original height property is lost and can't be reused.

The formal notation of the inheriting effect.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This two situations follow fixed rules described in the concordance table below:(add the table)

+---+------------+-----------+-----------+ 
| n | Lower node | Upper node| Properties|
+===+============+===========+===========+ 
| 1 | US/USM     | USV/s     | - material|
+---+------------+-----------+-----------+ 
| 2 | SF         |  VSF      |           |
+---+------------+-----------+-----------+
| 3 | Cells may  | - Cells   |           |
+---+ span rows. | - contain |           |
| 4 |            | - blocks. |           |
+---+------------+-----------+-----------+

In the first situation no formal notation is required: it is assumed by the human reader or evenutally from parsing algoritms.

In the second situation, the upper node (USV/s) will be connected with the USM node through a dotted line and a property node in the middle representing the name inheriting property (no descriprion is required in the description field.