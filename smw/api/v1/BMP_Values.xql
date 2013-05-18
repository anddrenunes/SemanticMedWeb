xquery version "3.0";
declare namespace mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1";
let $title := "BMP Average Values"
for $bmp in collection("/db/apps/mlhim-emr/data/care")//mlhim2:el-0c71fe4c-8dd2-4d0f-af05-15b5b7b9de24
  let $s := $bmp//mlhim2:el-f6c5ea6e-6458-4799-874d-7f3d365d260d/mlhim2:magnitude/text()
  let $g := $bmp//mlhim2:el-28f7ec54-254b-4b66-9c42-3b275fc1df38/mlhim2:magnitude/text()
  let $p := $bmp//mlhim2:el-781e9dda-055a-4a95-bee3-d482c44d1186/mlhim2:magnitude/text()
  let $u := $bmp//mlhim2:el-866aa21b-9cd2-48cc-9c18-8e799086d222/mlhim2:magnitude/text()
  let $c := $bmp//mlhim2:el-51b66f95-13b5-4e25-9c08-5e6d43aeba79/mlhim2:magnitude/text()

return
       <data>{$s},{$g},{$p},{$u},{$c}</data>
