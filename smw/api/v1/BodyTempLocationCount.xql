xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $title := "Body Temperature Location Counts"
let $vitals := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a4
  let $total := count($vitals)
  let $rcnt := count($vitals//mlhim2:el-779a5eeb-db86-414f-a7d7-7760e330ce0a[contains(mlhim2:DvString-dv,"Rectal")])
  let $ocnt := count($vitals//mlhim2:el-779a5eeb-db86-414f-a7d7-7760e330ce0a[contains(mlhim2:DvString-dv,"Oral")])
  let $fcnt := count($vitals//mlhim2:el-779a5eeb-db86-414f-a7d7-7760e330ce0a[contains(mlhim2:DvString-dv,"Forehead")])
  let $urcnt := count($vitals//mlhim2:el-779a5eeb-db86-414f-a7d7-7760e330ce0a[contains(mlhim2:DvString-dv,"Underarm, Right")])
  let $ulcnt := count($vitals//mlhim2:el-779a5eeb-db86-414f-a7d7-7760e330ce0a[contains(mlhim2:DvString-dv,"Underarm, Left")])

return
      <results>
      <ReportTitle>{$title}</ReportTitle>
      <rectal>{$rcnt}</rectal>
      <oral>{$ocnt}</oral>
      <forehead>{$fcnt}</forehead>
      <underarm-right>{$urcnt}</underarm-right>
      <underarm-left>{$ulcnt}</underarm-left>
      <Total>{$total}</Total>
      </results>