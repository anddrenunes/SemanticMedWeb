xquery version "3.0";
declare namespace xs = "http://www.w3.org/2001/XMLSchema";
declare namespace mlhim2 ="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
declare namespace rdfs = "http://www.w3.org/2000/01/rdf-schema#";
let $ct := collection("/db/apps/ismene/ccds")//xs:complexType

for $elem in $ct
return element semantics {
          for $child in $elem/(@*|text())
          return element {if ($child instance of attribute())
                          then name($child)
                          else 'value'} {
                    string($child)
                 }
       }