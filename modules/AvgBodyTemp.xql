xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $bt := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-6d79fc4b-e640-4ffb-a9c4-a28a585bba66/mlhim2:magnitude

return 
    <results>
    <body-temp-average>{avg($bt)}</body-temp-average>
    </results>