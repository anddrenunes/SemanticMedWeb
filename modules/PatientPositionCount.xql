xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $title := "BP Patient Position Counts"
let $vitals := collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a4
  let $total := count($vitals)
  let $sitcnt := count($vitals//mlhim2:el-186315c1-63f0-4880-a384-d850f159b36a[contains(mlhim2:DvString-dv,"Sitting")])
  let $pronecnt := count($vitals//mlhim2:el-186315c1-63f0-4880-a384-d850f159b36a[contains(mlhim2:DvString-dv,"Lying (Prone)")])
  let $standcnt := count($vitals//mlhim2:el-186315c1-63f0-4880-a384-d850f159b36a[contains(mlhim2:DvString-dv,"Standing")])

return
      <results>
      <ReportTitle>{$title}</ReportTitle>
      <sitting>{$sitcnt}</sitting>
      <prone>{$pronecnt}</prone>
      <standing>{$standcnt}</standing>
      <Total>{$total}</Total>
      </results>