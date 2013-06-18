xquery version "3.0";
module namespace ccdlib="http://www.semanticmedweb.com/demo/ccdlib";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_2";
declare namespace dc="http://purl.org/dc/elements/1.1/";
declare namespace rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#";

(: List all of the CCDs in the local library :)
declare function ccdlib:list($node as node(), $model as map(*), $coll as xs:string?){

let $lib := collection($coll)
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

(:View METADATA from an individual CCD selected from the library listing:)
declare function ccdlib:view-md($node as node(), $model as map(*), $id as xs:string?){

(: find schema id attribute :)
let $ccdid := concat('mlhim2-', $id)

(:setup the metadata variables :)
for $md in collection("/db/apps/smwdemo/ccdlib")  
let $title := $md//dc:title/text()
let $dcid := $md//dc:identifier/text()
let $creator := $md//dc:creator
let $contrib := $md//dc:contributor/text()
let $source := $md//dc:source/text()
let $rights := $md//dc:rights/text()
let $relation := $md//dc:relation/text()
let $coverage := $md//dc:coverage/text()
let $language := $md//dc:language/text()
let $publisher := $md//dc:publisher/text()
let $pubdate := $md//dc:date/text()
let $descr := $md//dc:description/text()
let $uri := $md/base-uri()
where $md//@id = $ccdid
  
return
<div class="meta-data">
  
  Title: <b>{$title} </b> ID: <b>{$dcid}</b><br/>
  Creator: <b>{$creator}</b> <br/>
  Contributors: <br/>


    {
      for $contrib in $md//dc:contributor
        return
        <div><b>{$contrib/text()}</b><br/></div>
   }


Keywords: <b>{$source} </b><br/>
License: <b>{$rights} </b> Coverage: <b>{$coverage}</b><br/>
Related To: <b>{$relation} </b> Language: <b>{$language}</b><br/>
Publisher: <b>{$publisher} </b> Date/Time Published: <b>{$pubdate}</b><br/>

<p><b>Description:</b><br/>{$descr}</p>
Source URI: {$uri}

</div>
};

(:View complexType data from an individual CCD selected from the library listing:)
declare function ccdlib:view-ct($node as node(), $model as map(*), $id as xs:string?){

(: find schema id attribute :)
let $ccdid := concat('mlhim2-', $id)

for $ccd in collection("/db/apps/smwdemo/ccdlib")
  for $ct in $ccd//xs:complexType
    let $ctname := $ct/data(@name)
    let $rmtype := $ct//xs:restriction/data(@base)[1] (: don't include enumeration restrictions :)
    let $doc := $ct/xs:annotation/xs:documentation/text()
    let $semantics := $ct/xs:annotation/xs:appinfo/rdf:Description//node()
    let $name := $ct//xs:sequence/xs:element[1]/data(@fixed)
    where $ccd//@id = $ccdid

return
<div>
<p>
Name: <b>{$name}</b>, Type: <b>{$rmtype}</b><br/>
CT: <b>{$ctname}</b> <br/>
Documentation: {$doc} <br/>
Semantic Link: {
  for $link in $semantics
  return <a href="{util:unescape-uri($link//data(@*),"UTF-8")}">{util:unescape-uri($link//data(@*),"UTF-8")}</a>
  }
</p>
</div>

};

