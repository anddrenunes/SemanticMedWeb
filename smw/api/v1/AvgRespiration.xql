xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $resp := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-b470da9b-5eda-4fe8-a629-d324e248c733/mlhim2:magnitude
  return <respirations-average>{avg($resp)}</respirations-average>