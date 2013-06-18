xquery version "3.0";
module namespace emrdata="http://www.semanticmedweb.com/demo/emrdata";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_2";
declare namespace dc="http://purl.org/dc/elements/1.1/";
declare namespace rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#";
declare namespace functx = "http://www.functx.com"; 

declare function functx:leaf-elements ($root as node()?) as element()* {
   $root/descendant-or-self::*[not(*)]
};

(: List all of the EMR Data :)
declare function emrdata:list-all($node as node(), $model as map(*)){

let $data := collection("/db/apps/smwdemo/data/emr/care")
for $instance in $data
  let $subject := $instance//mlhim2:cluster-subject[1]/text()
  let $path := document-uri($instance)
  let $file := tokenize($path, "/")[last()]
  where string-length($subject) > 1
  order by $file


return 
  <tr>
  <td>{$subject}</td><td><a href="emrdata-view.html?id={$path}">{$file}</a></td>
  </tr>
  };

(: List a specific instance of the EMR Data :)
declare function emrdata:view-instance($node as node(), $model as map(*), $id as xs:string?){

let $doc := doc($id)
let $ccd := $doc[1]/*/name()
let $entry := $doc/child::node()/child::node()
let $lang := $entry/mlhim2:language/text()
let $subject := $entry/*[3]/mlhim2:party-name/text()
let $provider := $entry/*[4]/mlhim2:party-name/text()

return 
  <p>
  CCD ID: {$ccd}, <br/>
  Language: {$lang}<br/>
  Subject of Record: {$subject}<br/>    
  Provider: {$provider}<br/>    
  </p>
  };

