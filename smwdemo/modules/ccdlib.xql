xquery version "3.0";
module namespace ccdlib="http://semanticmedweb.com/demo/ccdlib";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
declare namespace dc="http://purl.org/dc/elements/1.1/";

declare function ccdlib:view($node as node(), $model as map(*)){

let $lib := collection("/db/apps/smwdemo/ccdlib")
for $ccd in $lib
  let $title := $ccd//dc:title/text()
  let $descr := $ccd//dc:description/text()
  let $id := $ccd//dc:identifier/text()

return 
  <tr>
  <td>{$title}</td><td>{$descr}</td><td>{$id}</td>
  </tr>
  };