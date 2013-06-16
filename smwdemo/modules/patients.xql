xquery version "3.0";

(: 
 : Defines all the RestXQ endpoints used by the XForms.
 :)
module namespace pat="http://semanticmedweb.com/demo/patients";

import module namespace config="http://semanticmedweb.com/demo/config" at 'config.xqm';

declare namespace rest="http://exquery.org/ns/restxq";
declare namespace output="http://www.w3.org/2010/xslt-xquery-serialization";

declare variable $pat:data := $config:app-root || "data/emr";

(:~
 : List all addresses and return them as XML.
 :)
declare
    %rest:GET
    %rest:path("/address")
    %rest:produces("application/xml", "text/xml")
function demo:addresses() {
    <addresses>
    {
        for $address in collection($config:app-root || "/data/emr")/demog
        return
            $address
    }
    </addresses>
};

(:~
 : Test: list all addresses in JSON format. For this function to be chosen,
 : the client should send an Accept header containing application/json.
 :)
(:declare:)
(:    %rest:GET:)
(:    %rest:path("/address"):)
(:    %rest:produces("application/json"):)
(:    %output:media-type("application/json"):)
(:    %output:method("json"):)
(:function demo:addresses-json() {:)
(:    demo:addresses():)
(:};:)

(:~
 : Retrieve an address identified by uuid.
 :)
declare 
    %rest:GET
    %rest:path("/address/{$id}")
function demo:get-address($id as xs:string*) {
    collection($pat:data)/demog[@id = $id]
};

(:~
 : Search addresses using a given field and a (lucene) query string.
 :)
declare 
    %rest:GET
    %rest:path("/search")
    %rest:form-param("query", "{$query}", "")
    %rest:form-param("field", "{$field}", "name")
function demo:search-addresses($query as xs:string*, $field as xs:string*) {
    <addresses>
    {
        if ($query != "") then
            switch ($field)
                case "name" return
                    collection($pat:data)/demog[ngram:contains(name, $query)]
                case "street" return
                    collection($pat:data)/demog[ngram:contains(street, $query)]
                case "city" return
                    collection($pat:data)/demog[ngram:contains(city, $query)]
                default return
                    collection($pat:data)/demog[ngram:contains(., $query)]
        else
            collection($pat:data)/demog
    }
    </addresses>
};

(:~
 : Update an existing address or store a new one. The address XML is read
 : from the request body.
 :)
declare
    %rest:PUT("{$content}")
    %rest:path("/address")
function demo:create-or-edit-address($content as node()*) {
    let $id := ($content/demog/@id, util:uuid())[1]
    let $data :=
        <address id="{$id}">
        { $content/demog/* }
        </address>
    let $log := util:log("DEBUG", "Storing data into " || $pat:data)
    let $stored := xmldb:store($pat:data, $id || ".xml", $data)
    return
        demo:addresses()
};

(:~
 : Delete an address identified by its uuid.
 :)
declare
    %rest:DELETE
    %rest:path("/address/{$id}")
function demo:delete-address($id as xs:string*) {
    xmldb:remove($pat:data, $id || ".xml"),
    demo:addresses()
};