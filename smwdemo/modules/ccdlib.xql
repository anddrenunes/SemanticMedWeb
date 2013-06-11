xquery version "3.0";
module namespace ccdlib="http://semanticmedweb.com/demo/ccdlib";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_2";
declare namespace dc="http://purl.org/dc/elements/1.1/";
declare namespace rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#";

declare function ccdlib:list($node as node(), $model as map(*)){

let $lib := collection("/db/apps/smwdemo/ccdlib")
for $ccd in $lib
  let $title := $ccd//dc:title/text()
  let $descr := $ccd//dc:description/text()
  let $id := $ccd//dc:identifier/text()
  order by $title

return 
  <tr>
  <td><a href="ccdview.html?id={$id}">{$title}</a></td><td>{$descr}</td><td>{$id}</td>
  </tr>
  };
  
declare function ccdlib:view($node as node(), $model as map(*), $id as xs:string?){

let $ccdid := concat('mlhim2-', $id)
for $ccd in collection("/db/apps/smwdemo/ccdlib")  
let $title := $ccd//dc:title/text()
let $dcid := $ccd//dc:identifier/text()
let $creator := $ccd//dc:creator
let $contrib := $ccd//dc:contributor/text()
let $source := $ccd//dc:source/text()
let $rights := $ccd//dc:rights/text()
let $relation := $ccd//dc:relation/text()
let $coverage := $ccd//dc:coverage/text()
let $language := $ccd//dc:language/text()
let $publisher := $ccd//dc:publisher/text()
let $pubdate := $ccd//dc:date/text()
let $descr := $ccd//dc:description/text()
let $uri := $ccd/base-uri()
where $ccd//@id = $ccdid


  
return
<div>
Title: <b>{$title} </b> ID: <b>{$dcid}</b><br/>
Creator: <b>{$creator}</b> Contributors: <b>{$contrib}</b> <br/>
Keywords: <b>{$source} </b><br/>
License: <b>{$rights} </b> Coverage: <b>{$coverage}</b><br/>
Related To: <b>{$relation} </b> Language: <b>{$language}</b><br/>
Publisher: <b>{$publisher} </b> Date/Time Published: <b>{$pubdate}</b><br/>

<p><b>Description:</b><br/>{$descr}</p>
Source URI: {$uri}
<p>
<b>Structure: </b><br/>
<div content-type="application/xml">
<code>{$ccd}</code>
</div>
</p>
</div>
};

