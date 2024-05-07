# Events and Event Handling


#### Definition

**Event:** In JavaScript, an event is a signal that something has happened in the web page or application. This could be user interactions like clicks, key presses, or page loading.

**Event Handling:** Event handling in JavaScript refers to the process of writing code to respond to events. This involves attaching event listeners to specific elements in the DOM (Document Object Model) and defining functions that are executed when the specified event occurs. Event handling allows developers to create interactive and dynamic web experiences.



#### Question 1

Make the filter work

#### Solution

**Parent element:** This is a property which will get the parent element from the DOM tree of a specific child.

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/278/original/upload_4c37b0f4e346d0b8f6bf6f51f07d2c7a.png?1695147551)


```javascript
<!DOCTYPE html>
<html lang = "en">
  <head>
    <meta charset = "UTF - 8" />
    <meta http - equiv = "X - UA - Compatible" content = "IE = edge" />
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0" />
    <title>Document</title>
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        padding-top: 5rem;
      }

      .movies {
        height: 10rem;
        width: 10rem;
        margin: 2rem;
      }

      .price {
        background-color: rgb(247 84 33);
        height: 8rem;
        padding: 1.5rem;
        font-size: 2rem;
      }

      .heading {
        background-color: rgba(0, 0, 0, 0.856);
        height: 2rem;
      }

      .heading,
      .price {
        color: white;
        text-align: center;
        margin: 0;
      }

      select,
      h1 {
        position: fixed;
      }

      h1 {
        top: 0px;
      }

      select {
        width: 8rem;
      }


    </style>
  </head>

  <body>
    <h1>BOOK MY SHOW</h1>
    <select>
      <option value = "none">None</option>
      <option value = "action">Action</option>
      <option value = "romance">Romance</option>
      <option value = "comedy">Comedy</option>
    </select>

    <div class = "movies">
      <h3 class = "heading">Action Movie - 1</h3>
      <p class = "price" data-category = "action">Rs. 100</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Action Movie - 2</h3>
      <p class = "price" data-category = "action">Rs 200</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Action Movie - 3</h3>
      <p class = "price" data-category = "action">Rs. 150</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Romance - 1</h3>
      <p class = "price" data-category = "romance">Rs 200</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Romance - 2</h3>
      <p class = "price" data-category = "romance">Rs. 150</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Romance - 3</h3>
      <p class = "price" data-category = "romance">Rs. 150</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Action Movie-4</h3>
      <p class = "price" data-category = "action">Rs 200</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Comedy - 1</h3>
      <p class = "price" data-category = "comedy">Rs. 100</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Romance - 4</h3>
      <p class = "price" data-category = "romance">Rs. 100</p>
    </div>
    <div class = "movies">
      <h3 class = "heading">Comedy - 2</h3>
      <p class = "price" data-category = "comedy">Rs 200</p>
    </div>
    <script>
      // Q Make the filter work

      let select = document.querySelector('select')

      select.addEventListener('change' , function(){
        let filterVal = select.value

        // console.log(filterVal)

        let allTickets = document.querySelectorAll('.price')

        if(filterVal == 'none'){
          for(let i = 0 ; i < allTickets.length ; i ++ ){
            allTickets[i].parentElement.style.display ='block'
          }
        }

        else{
             for(let i = 0 ; i < allTickets.length; i ++ ){
               if(allTickets[i].getAttribute('data-category') != filterVal){
                allTickets[i].parentElement.style.display ='none'
               }
               else{
                allTickets[i].parentElement.style.display ='block'
               }
             }
        }
      })
    </script>
  </body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/281/original/upload_fd792df135de98bd7dc930ac5ea9316e.png?1695147830)


#### Question 2

Implement key taps such that on pressing 1 you scroll to section 1,  pressing 2 you scroll to section 2 and  pressing 3 you scroll to section 3. Also implement key tap b to go to bottom of the page and key tap t to go to top of the page

#### Solution

```javascript
<!DOCTYPE html>
<html lang = "en">
  <head>
    <meta charset = "UTF-8" />
    <meta http - equiv = "X-UA-Compatible" content = "IE = edge" />
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0" />
    <title>Document</title>
    <style>
      p {
        font-size: 1.5rem;
      }
    </style>
  </head>
  <body>
    <h1>
      Press 1 to go to Section-1 <br />
      Press 2 to go to Section-2 <br />
      Press 3 to go to Section-3 <br />
      Press t to go to top of the page <br />
      Press b to go to bottom of the page
    </h1>

    <h2 id = "s1">Section 1</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Excepturi ipsum
      rem placeat ullam vero animi adipisci laboriosam libero quidem quisquam
      quam quae veniam, exercitationem aspernatur quaerat qui harum maiores
      tenetur vel magnam temporibus dolor modi deserunt. Excepturi nesciunt sint
      velit blanditiis provident modi voluptate, corrupti fugit est minima quae
      qui praesentium minus cupiditate aut! Ipsam voluptatum dolores hic quis
      iure ipsa, aperiam deserunt harum aspernatur similique laudantium a eaque,
      sint obcaecati, ut consequuntur eum? Officia delectus quis qui velit
      minima assumenda ipsa, quos natus quae amet sequi laudantium cumque sit
      aliquam perspiciatis tenetur ad illum quaerat aperiam aspernatur beatae?
      Cupiditate dolorum modi aut odio debitis esse ad nesciunt suscipit magnam
      quis alias tempora asperiores, optio quisquam sapiente blanditiis ducimus
      eveniet quasi sed ipsa iure aliquid. Sapiente minima recusandae nesciunt,
      magni atque vel quidem quibusdam numquam velit quas fuga, in rem.
      Blanditiis delectus tempora eius possimus minima, necessitatibus error,
      similique rerum incidunt iure amet explicabo iusto. Incidunt laudantium
      ipsa hic tenetur perspiciatis, expedita beatae modi voluptatem delectus
      veniam dolores numquam. Maiores fugit, quidem ad id voluptates vel.
      Dolores consequuntur recusandae voluptatum voluptatibus ipsum fugit soluta
      voluptatem adipisci sint molestiae! Cum itaque repudiandae asperiores quas
      ratione molestiae, quaerat, quam, sint illo a consequuntur odit ullam
      accusamus! Adipisci asperiores aut laboriosam facilis non illo voluptas
      vitae, obcaecati deserunt, assumenda perferendis similique optio, ullam
      earum quasi. Nostrum necessitatibus illo voluptas modi repellendus id eum
      ducimus? Voluptatum fugit maiores voluptate, quod suscipit, excepturi quas
      nam minus rem, illum consectetur! Aliquam voluptatibus a molestias
      officiis qui nobis ratione ex quidem minima saepe maiores voluptates
      corporis provident, pariatur fugiat expedita omnis numquam voluptas
      sapiente fugit nesciunt laboriosam eligendi. Voluptatibus quo, impedit
      nemo error mollitia maiores soluta tempore repellendus nesciunt, vel hic
      quidem voluptatem commodi quia, voluptas deleniti reiciendis magnam
      aliquam delectus dolore iusto sint. Possimus, numquam, dignissimos cum
      sint consequatur molestias, nemo dicta doloribus adipisci amet consectetur
      iste qui. Fugiat mollitia itaque odio, commodi et voluptates obcaecati
      iure assumenda ab amet voluptate tempora vitae a alias adipisci nesciunt
      laboriosam sit natus. Consectetur accusantium iure voluptates libero
      eligendi non eveniet perferendis minus perspiciatis numquam eius, adipisci
      ducimus maiores saepe neque quidem tempore nostrum rem beatae nulla omnis
      expedita sunt autem? Dignissimos sint tempore mollitia obcaecati animi
      pariatur ipsam nemo vitae doloremque in omnis ex corporis expedita natus,
      aliquid quod esse quos praesentium culpa, veniam quo? Eum nesciunt, est
      laudantium earum omnis sequi. Delectus est velit tenetur iusto minima
      vero, quidem natus, placeat, aspernatur atque quibusdam dolorem quisquam
      blanditiis porro explicabo repellendus modi. Nam beatae natus accusamus
      quos impedit adipisci corporis fugiat architecto hic ut odio perferendis
      placeat obcaecati ullam tempore et cumque eum sunt, dignissimos quibusdam
      quaerat minima numquam rem. Unde eum culpa ullam, deleniti quae quos
      dolorem, corrupti cupiditate, repellendus impedit tenetur repellat
      voluptates aliquid possimus in sed dolore quam aut ex eius rem corporis
      nulla enim doloribus. Id quam impedit doloremque explicabo temporibus,
      nisi quos dolore earum, dolores deleniti sint eum quidem. Voluptas magnam
      quod, eius labore amet ipsam veniam sapiente, quos neque commodi eligendi
      quasi nulla cupiditate quidem sequi nesciunt. Assumenda praesentium
      debitis reiciendis alias qui, porro autem libero numquam omnis mollitia
      cupiditate. Ex blanditiis maiores aliquam labore suscipit, distinctio hic
      ab quaerat, ut soluta consequatur pariatur aperiam iste quidem voluptates
      saepe, facilis ipsum doloremque? Quidem tenetur eaque, sunt inventore
      laudantium explicabo laborum similique vitae sequi autem aspernatur?
      Consequatur ullam natus porro reiciendis officiis. Vero, consequatur
      itaque? Repellendus dolor voluptate aut voluptatum libero tenetur natus
      dicta dolorum assumenda quae. Error nam dolores voluptatibus consectetur
      repudiandae laudantium deleniti quaerat consequatur, porro, aliquid at
      dicta libero quidem, suscipit facilis sed aspernatur ab in rerum non.
      Tempore aut dolores, assumenda mollitia dicta, neque minima explicabo
      excepturi, eveniet nobis nulla tenetur. Pariatur dolore dolorum nobis
      commodi, quo amet saepe quae magnam eius! Ex vero consectetur delectus
      aliquid! Minima culpa possimus dicta iste excepturi aut quia officiis
      reiciendis animi perspiciatis neque, deserunt minus beatae voluptates
      veritatis rerum tempore molestias reprehenderit dolorem suscipit
      repellendus esse non optio? Necessitatibus magni alias cumque repellendus
      blanditiis tempora incidunt beatae labore in explicabo illo enim nisi quos
      corrupti dolor adipisci ipsam, reprehenderit dolores vero. Labore ad, non
      quos nam reiciendis sapiente molestias nobis, facilis placeat voluptatibus
      perspiciatis dolorem voluptatem ipsum. Sint accusantium libero, fugiat
      quibusdam delectus quia nostrum minima sequi illo quidem magni rem ex et
      quasi ab error omnis eligendi odit repellat provident expedita
      perspiciatis iusto! Adipisci, molestiae! Eaque delectus molestiae facilis
      amet quis sed laudantium, quas ullam inventore ipsum nam adipisci hic?
      Magnam nulla culpa pariatur at. Rem alias, ducimus ea atque omnis culpa
      fuga, pariatur vel unde ad expedita in aliquid consequuntur excepturi.
      Veritatis quia, voluptatum repellat quos ipsa dignissimos recusandae
      delectus quaerat dolore reprehenderit. Fugiat, voluptate quibusdam. Ea
      amet atque, veniam ullam labore nesciunt eveniet? Nulla reiciendis
      accusamus ipsam laboriosam officia, provident corporis porro sunt!
      Corporis incidunt tempora, quod unde quae alias repellat odio ea quisquam
      quos beatae? Tempora, nisi doloremque! Ea enim, quos cum repudiandae sequi
      ut mollitia qui quidem inventore molestiae corrupti exercitationem cumque
      minima? Optio consequuntur porro saepe tempora excepturi nihil facere
      facilis doloribus vero totam quae aut illum adipisci dolores provident
      sunt, voluptatum vitae iure id nulla beatae non quaerat accusamus. Vitae
      magni cum ab dolores eum sint consectetur laborum, quam magnam iste itaque
      similique, modi ducimus non a aliquam corporis nam earum delectus tempora
      expedita officia! Ducimus, officiis id rem officia, ipsa atque fugit
      quisquam provident nobis ullam alias aperiam, minus quo ipsum quibusdam.
      Delectus corrupti suscipit sed nobis temporibus sapiente quas illum,
      pariatur sint deserunt incidunt reiciendis doloribus unde numquam ut,
      quisquam, doloremque quod non? Unde nisi dolorem repudiandae iusto nulla,
      perspiciatis eligendi magnam sequi assumenda non quam repellat natus
      consectetur harum, architecto qui. Aliquid, iste pariatur! Expedita
      explicabo molestias possimus laborum voluptates maiores, accusantium
      voluptate eos excepturi dignissimos eveniet earum placeat! Velit cumque
      facilis dolorem, maiores quidem dolores tenetur amet fugiat similique
      doloribus porro exercitationem, laboriosam rerum nihil, praesentium odio.
      Animi soluta quia totam vero, necessitatibus ratione debitis omnis atque
      officiis consequatur esse libero nulla assumenda fugiat non rerum
      asperiores ullam ipsam quam harum amet? Blanditiis, error officia!
      Architecto maiores tempora sit error eum ducimus, consequuntur laudantium
      fuga reprehenderit voluptas alias magnam distinctio nisi eveniet maxime
      vel dolores repudiandae assumenda officia doloribus saepe nemo, molestias
      minima. Neque iusto, ullam repellendus quidem nostrum temporibus deleniti
      itaque dolore aliquid eveniet, molestias exercitationem corrupti molestiae
      fugit tenetur perferendis quibusdam iste esse sapiente nam praesentium
      consequuntur? Inventore ipsa natus neque assumenda. Cupiditate ex nobis
      deserunt laudantium ratione asperiores porro voluptate debitis culpa,
      explicabo, cum vel. Nulla delectus vitae voluptatibus facere nisi ab modi
      exercitationem ipsam inventore in illum recusandae, cumque iste nemo
      laborum, nihil autem libero accusamus expedita quasi ea maiores? Aperiam
      eveniet officia id officiis in excepturi quae, vel illo? Commodi quis
      libero cupiditate, quae praesentium at consequatur ipsa necessitatibus
      veniam optio nam ipsam voluptatem officiis omnis voluptate id
      exercitationem sunt vero fugiat explicabo, quidem beatae aspernatur porro
      voluptatum? Nisi ipsam quisquam ipsum incidunt repellendus? Perferendis
      dignissimos dolorum soluta quaerat. Eaque odit perferendis quasi vero
      dolorum eius accusamus atque, autem a dicta architecto facere. Nostrum et
      possimus cum, a perferendis ducimus laudantium harum? Hic voluptatum quam,
      assumenda ipsa quod nemo possimus temporibus blanditiis sequi rerum
      obcaecati iusto quidem dolore libero adipisci non, nulla pariatur quo,
      ducimus quos perferendis corporis. Quos totam laboriosam consectetur,
      quaerat similique unde, earum aliquid magni molestias at esse porro
      perspiciatis, alias voluptatem? Alias consequatur nostrum voluptatum,
      doloribus adipisci aperiam pariatur magni aspernatur cum repellat vero
      debitis corrupti deleniti sequi vel modi harum in? Reiciendis quas
      voluptatibus veniam earum delectus cum soluta harum. Distinctio enim,
      repellendus alias labore id, eveniet cum repudiandae commodi, doloribus
      animi eaque exercitationem? Quas nobis reprehenderit quis ut dolorem
      obcaecati sequi recusandae perferendis facere. Magnam voluptatibus
      asperiores ratione voluptate hic repellat reprehenderit sequi quisquam.
      Consequuntur quos, explicabo delectus beatae labore tenetur perspiciatis
      ipsum consequatur obcaecati sunt necessitatibus est dolorem vero odit
      exercitationem nam architecto itaque iusto fugit consectetur rerum
      laboriosam rem ducimus ad? Tempore, soluta eius id sed, expedita
      consectetur unde consequatur doloremque iure dolore enim molestias maiores
      commodi cum vitae aut aliquid, sapiente sit dicta assumenda quibusdam. Et,
      distinctio voluptatem voluptas omnis eaque qui sapiente dicta voluptate
      quos dolores vel magni inventore sunt quisquam ipsa recusandae eveniet
      quibusdam, saepe repudiandae itaque quia doloremque mollitia quis nobis!
      Sapiente dolorem quae fugiat deleniti molestias fuga odit eveniet
      voluptatibus nostrum beatae porro dolore soluta officiis, aspernatur,
      sequi est! Blanditiis velit et dolor, aut deserunt quod quasi totam! Ipsam
      perferendis culpa maxime! Aliquid quisquam delectus eum iste consectetur
      sit labore voluptas? Autem voluptatibus, excepturi numquam repellendus
      quaerat dolorem, obcaecati eum inventore qui similique odit, optio
      adipisci consequatur. Ullam sequi reiciendis harum in amet eligendi eum
      recusandae. Deleniti ullam facilis voluptatem blanditiis recusandae!
      Provident animi porro architecto earum sunt soluta voluptas eaque quaerat
      hic odio deleniti impedit velit qui alias corporis sed, obcaecati
      consequatur quo omnis sit et. Deleniti ea delectus non iusto expedita
      laborum, itaque nesciunt nisi inventore recusandae eveniet. Reprehenderit
      nesciunt fugit atque iste omnis error possimus molestias laudantium at,
      culpa natus amet qui dolore sint commodi adipisci repudiandae dignissimos
      voluptate provident illum quo! Iusto natus illum nisi harum dolore culpa,
      corrupti doloribus nesciunt sed consequatur animi adipisci ratione, odio
      soluta reiciendis veniam dicta dolores est et maiores eius nostrum totam
      quidem. Magnam aperiam nisi ut maxime aspernatur, autem dolorum cum, ex
      laborum temporibus, neque necessitatibus fugiat! Dignissimos corrupti
      doloribus voluptate nam deleniti saepe, dolor sit. Voluptatem autem
      reiciendis suscipit ut porro optio delectus dolores iusto, molestiae vel
      quos eaque esse, fugit facere. Amet quod distinctio, illum ullam possimus
      laborum aut explicabo eos tempore repellendus dolorem sunt tempora
      eligendi laboriosam sit temporibus aperiam similique. Accusantium labore
      eligendi animi adipisci magni, veritatis non libero! Asperiores doloribus
      fugit, fugiat distinctio consequatur tempora totam illo iste earum, unde
      accusantium enim similique! Quidem cupiditate culpa, dignissimos unde sint
      nihil fugit commodi nemo odio at facilis eveniet. Molestias vel neque id
      quas a delectus pariatur iure eaque vitae ea, deserunt laborum repellat,
      voluptatum beatae ducimus perspiciatis dolorem libero repellendus error
      possimus, alias maxime? Molestiae vitae iusto veniam quo et exercitationem
      eos suscipit tenetur incidunt eaque ducimus quaerat eum ex autem, quia
      eveniet iure laboriosam, placeat cupiditate porro, obcaecati impedit atque
      expedita? Impedit, accusantium? Similique exercitationem est eaque
      deserunt quibusdam vitae recusandae, quaerat, esse numquam quasi porro
      necessitatibus velit dignissimos quas rem possimus ipsum ducimus quod
      adipisci vero qui dicta, dolor nam. Tempore expedita laudantium facilis!
      Ab saepe nostrum a tempora, sequi nihil est unde eos quas voluptate,
      libero reprehenderit molestiae numquam dolorem pariatur distinctio
      veritatis accusamus alias. Nisi iure quasi dicta repellat placeat, quis
      inventore? Doloribus, distinctio consequatur! Fuga deleniti placeat
      perspiciatis mollitia sequi labore cupiditate minus cum assumenda,
      quibusdam quia accusantium natus expedita porro quasi voluptatibus magni
      esse nihil illum id illo. Quos ipsa magni facilis sed distinctio cum
      aspernatur necessitatibus, voluptates temporibus officiis placeat qui
      saepe provident enim fugit voluptate minima repellat labore dolores, vero
      velit amet nesciunt esse? Delectus eligendi ullam accusamus consequatur
      blanditiis aspernatur maiores libero neque dolor quae fugit, alias
      repellat ex unde fuga est. Quibusdam pariatur rerum dicta similique
      facilis rem voluptatibus. Doloremque, quisquam similique! Odit incidunt
      quos illo ex voluptatibus, nam blanditiis rerum accusamus aperiam atque
      magni quidem tenetur et vero voluptate nihil quisquam beatae ducimus optio
      voluptas laboriosam! Accusamus odio nesciunt, beatae molestiae dolore
      cupiditate eum, sit repudiandae iusto natus minima vitae quas sint. Harum,
      repellat. Odio cum, pariatur tempora aliquid perspiciatis reiciendis sed
      similique non numquam veritatis doloremque sit velit placeat laborum
      quasi. Odio excepturi vitae distinctio cum sint quos adipisci perferendis
      cupiditate assumenda eveniet! Nisi corporis id quis culpa adipisci,
      aliquid praesentium laudantium tempora beatae at totam iste et quae,
      quidem aliquam numquam aperiam. Ipsum ea pariatur itaque maiores, tenetur
      unde, sit, enim exercitationem officiis ducimus consectetur ipsa deserunt.
      Laudantium inventore tempore impedit dolorum similique assumenda officia,
      nulla quas deserunt sit? Ut reiciendis officiis vitae dolorem nobis illo
      hic dolor quasi, suscipit aut enim necessitatibus, amet incidunt sunt
      magni unde? Dicta odio voluptas, perspiciatis porro possimus esse
      praesentium tempora, tempore et, eos cum ea architecto molestias veritatis
      at quia? Similique, nemo! Sint quo soluta corporis assumenda magni. Lorem
      ipsum dolor sit amet consectetur adipisicing elit. Officia praesentium
      reprehenderit vero ratione quia quaerat rerum dicta quidem accusamus.
      Dolorem molestias qui nam aperiam vitae asperiores optio voluptatibus quae
      sit repellendus facilis sunt cum consectetur officiis, harum fugit magni!
      Velit placeat corporis beatae sed ea quae impedit molestias tempora
      blanditiis, maiores porro molestiae iure saepe repellat veritatis error
      ullam sapiente optio quia. Illo aliquid quo quaerat, consequatur nemo
      recusandae pariatur quae odio nam ut natus laboriosam cum voluptatibus!
      Dolores, ut cupiditate nisi numquam adipisci ullam minima architecto
      consequuntur inventore veritatis, possimus dolorum ipsam expedita
      accusamus repellat fugiat id vitae. Dolor inventore porro iusto quisquam
      dolorum nihil, deserunt laborum accusantium expedita nostrum corporis
      aliquam, exercitationem, consequuntur aut doloremque magnam architecto
      voluptates. Eos laudantium veniam praesentium sit vero saepe natus quaerat
      rem ut veritatis molestias non provident repellat labore totam voluptates
      ullam mollitia alias, aut modi, dolorem nostrum! Repellat, laboriosam
      voluptates inventore similique deleniti sit ea odit, minima consectetur
      ducimus possimus officia quam at? Saepe exercitationem temporibus quaerat
      eum ipsam animi, dolores voluptates dignissimos nisi tenetur voluptas
      eveniet aut fugiat impedit facilis recusandae sapiente? Accusantium
      dignissimos, voluptate vel cumque illum quisquam culpa Lorem ipsum dolor,
      sit amet consectetur adipisicing elit. Beatae et consectetur, qui officia
      libero a tenetur facere ex dolore accusantium debitis, hic, culpa
      distinctio atque fugiat tempora temporibus excepturi inventore nam aliquid
      quia facilis reprehenderit ut. Enim, illum voluptas ipsum quibusdam
      commodi assumenda. Reiciendis, harum sapiente laudantium officiis pariatur
      tenetur nostrum ipsa quibusdam corporis sit quam velit. Lorem ipsum, dolor
      sit amet consectetur adipisicing elit. Culpa cum minima iste eligendi enim
      ea quam exercitationem modi, similique saepe cupiditate incidunt
      laudantium facere nostrum inventore porro nobis rerum dicta aspernatur
      quia excepturi nesciunt vero. Quo vel, fugit, hic voluptatibus adipisci
      repudiandae dolore veritatis laboriosam distinctio incidunt nisi sapiente
      quibusdam ducimus officiis ut a esse beatae amet quia, animi velit.
      Ratione neque exercitationem, illo culpa placeat voluptatibus
      reprehenderit beatae unde omnis asperiores quam sequi vel aspernatur fuga
      deserunt laboriosam numquam labore sunt voluptatem? Illum soluta saepe ad
      blanditiis odio accusamus quia. Temporibus veniam deleniti debitis
      deserunt? Eveniet et laboriosam velit provident quasi quaerat quibusdam
      eos, animi vel. Amet placeat velit, aspernatur voluptatem quidem
      reiciendis impedit totam fuga labore perspiciatis officia commodi repellat
      modi nisi. Aut asperiores ad repellat mollitia vel illum, sunt distinctio
      corrupti inventore quos hic quas facilis molestias unde minus dicta rem
      maiores eveniet soluta quia maxime iste provident nesciunt voluptatibus!
      Expedita, dolorum blanditiis magnam porro accusamus asperiores beatae ex
      molestias odit neque quo repellendus aperiam ea voluptate a enim iure
      numquam fugit tenetur! Harum accusantium molestias ipsa consectetur
      eligendi, deserunt praesentium ratione non aliquid quo recusandae quas
      libero distinctio dicta et, in quos doloribus sit labore vel cupiditate
      minima iste officia repudiandae. Nemo impedit sit itaque rerum soluta quos
      facilis praesentium alias illum necessitatibus cumque excepturi doloremque
      laboriosam dolorum blanditiis eos hic pariatur est debitis, maiores
      voluptatum nisi. Totam, soluta nesciunt pariatur, odio doloribus nobis
      error debitis enim facere cupiditate velit maxime earum itaque quibusdam
      voluptatibus modi ut, hic esse? Ex nobis neque itaque pariatur eius ab
      incidunt nisi ullam laboriosam quibusdam voluptatibus dolores suscipit,
      minus nostrum, deleniti iusto reiciendis. Accusamus iste est commodi
      accusantium delectus. Tenetur rerum maiores sed odit dolores. Odio
      assumenda dolorem maiores doloremque dicta aliquam rem enim numquam est
      voluptate sed corporis facere illo molestias sit at, minus reiciendis
      eaque repellat? Voluptates quo maxime eum quasi totam odit laborum
      molestiae sunt cupiditate numquam? Dignissimos similique reprehenderit,
      repellendus placeat, vel fugiat id labore nemo ab a explicabo itaque nisi
      saepe quidem magni impedit pariatur odio, et consectetur ducimus quos
      laborum voluptas vitae eveniet! Beatae doloremque omnis, hic accusantium
      explicabo quaerat obcaecati quae aspernatur illum natus, repellat
      perspiciatis et asperiores provident totam. Doloribus odio sequi, fugiat
      repudiandae minima soluta tempora vitae explicabo voluptas officia
      distinctio cupiditate adipisci unde. Aspernatur, inventore quasi.
      Quisquam, in fugiat doloribus vel omnis similique dolorem, inventore est
      esse eum perspiciatis minus vero molestiae explicabo delectus libero ab
      repudiandae? Est rem magnam exercitationem quia, quaerat excepturi
      voluptatibus provident asperiores eius qui molestias laborum nemo dolor
      officiis ab explicabo tempora tenetur nisi harum repellat consequatur
      doloremque. Vel, ut deserunt. Numquam alias labore officia nam modi,
      minus, temporibus voluptates libero doloribus quasi maxime similique
      magnam est atque, omnis doloremque nisi tempora eaque beatae velit! Rerum
      ipsum laborum, numquam nesciunt placeat recusandae corrupti neque at
      molestiae sint odit ipsam provident necessitatibus voluptate ipsa
      explicabo perferendis magni ab magnam praesentium voluptatum suscipit
      aperiam dolores. A explicabo cupiditate nostrum iusto distinctio
      voluptatum quam expedita, magni assumenda atque adipisci fuga pariatur,
      quod exercitationem aspernatur maiores corporis sequi, accusantium
      voluptas molestiae aliquid fugit eius tempora dolore. Assumenda sed
      accusantium quia quisquam necessitatibus officiis modi in, quos,
      laudantium maxime asperiores officia. Asperiores provident, nisi voluptate
      debitis praesentium quaerat amet temporibus hic tempora dignissimos,
      officia reprehenderit natus veniam nostrum blanditiis, numquam molestiae
      sit culpa consectetur facere aliquam adipisci! Nam, corrupti voluptatibus
      molestias placeat quo rem laboriosam magnam consectetur iste ullam
      sapiente distinctio error iusto id optio pariatur ea excepturi vitae?
      Magnam tempore mollitia ex necessitatibus? Numquam corporis, aliquam vitae
      porro consectetur doloribus tempora libero vero eos quibusdam distinctio
      ullam? Alias, ullam sequi minus debitis dolorum animi nulla fugit, eos ex,
      saepe at quibusdam libero odit repudiandae? Dignissimos, aut sint.
      Deserunt est error, provident, soluta fuga alias possimus molestias
      laborum quasi dolorum a. Nesciunt consequatur porro distinctio tenetur
      possimus, iure sit deserunt veniam omnis amet reiciendis. Temporibus odio
      recusandae delectus impedit totam consequatur beatae corrupti id esse
      repudiandae, sed ut saepe voluptatem nisi accusamus similique quisquam
      excepturi amet. Harum rem consequatur mollitia minima at vitae corporis
      quis cupiditate iste maiores praesentium dolorem culpa reprehenderit
      officiis, eaque voluptatum accusantium dolores natus asperiores odit vel
      neque. Fugit, sit error ipsa in alias atque numquam explicabo odio natus
      harum, id nam! Repellendus obcaecati illum doloribus facilis. Delectus
      voluptatem maxime nobis deserunt eius eaque magni voluptas tempora hic
      eveniet, laborum neque, minima, velit possimus. Assumenda consequatur quas
      consectetur rem labore aspernatur, esse quaerat, ipsum iure maxime autem
      necessitatibus veritatis similique suscipit impedit facere odio doloribus
      dolores incidunt laudantium. Quaerat doloremque vel velit impedit
      molestias consequuntur, provident animi officiis ipsam expedita suscipit.
      Laborum alias quas veniam. Quos deserunt sapiente ex doloremque, expedita
      architecto autem consequuntur. Commodi nobis voluptatibus cupiditate
      accusantium iure molestias repellat, cumque voluptate distinctio, eum modi
      voluptates, dignissimos illum molestiae eius magnam consectetur
      consequatur hic? Quo hic quod labore ex quisquam quos error nesciunt
      itaque cupiditate odit minus quasi dolorum non officiis doloremque,
      consequatur id rerum explicabo recusandae! Reiciendis accusamus
      consequatur corporis recusandae cupiditate libero illum aperiam.
      Similique, atque deserunt sequi, quis, est id libero earum iusto hic
      provident vel. Cupiditate, provident tempore voluptatum quibusdam id earum
      sequi mollitia vitae aliquid, soluta iure veritatis officiis ipsum
      incidunt non eum quos hic! Fugiat ut dicta dignissimos earum, alias iste
      officia quidem placeat nesciunt officiis et magni autem fuga voluptates
      temporibus porro numquam sint facilis dolorem aut aliquam ex tenetur
      reiciendis. Commodi at aperiam hic sequi, ratione perferendis a qui
      eligendi fuga optio nihil vel minus, facilis quos! Consectetur nesciunt
      corporis odit temporibus officia porro, numquam, ratione cupiditate,
      possimus deleniti nam. Dolorem blanditiis ad saepe odio dolorum veniam
      doloremque error in voluptates eos ea asperiores itaque, dicta dolor quasi
      nulla quis alias aliquid, nobis eveniet. Nam quam nisi architecto, eius
      magnam aut exercitationem aspernatur doloribus, iusto, fugit amet quod
      odio temporibus. Consectetur aspernatur ab voluptatem, in voluptatum
      excepturi magni hic non, itaque ad quisquam! Ex inventore repellat magni
      quaerat assumenda magnam adipisci consectetur sit explicabo officiis
      possimus optio, voluptas doloribus rerum, doloremque similique sapiente
      commodi. Eligendi ea porro, ad praesentium recusandae vitae laudantium
      sunt placeat numquam tempora rerum nobis, eum cumque magnam non.
      Aspernatur quae dolore nemo quasi saepe, id blanditiis repudiandae
      provident molestias rerum nesciunt similique quos eaque ab facere earum
      dolor illo ipsam? Debitis enim eius sint sequi dignissimos ipsa unde,
      natus repudiandae accusamus laborum iste esse, quod, non ex praesentium
      repellat ullam sapiente perferendis dolores? Impedit sequi consectetur
      velit pariatur facilis omnis perspiciatis odit officiis libero, optio
      delectus labore ullam unde a voluptate? Consectetur saepe sed harum fugit
      magnam accusamus labore ab repudiandae aperiam quae blanditiis pariatur a
      officiis ut esse eligendi amet veniam maiores architecto soluta magni,
      ipsam repellendus dolores? Dolor libero sapiente non officia ullam quis
      quas tenetur itaque laudantium consectetur fugiat deleniti repellat rem
      dicta, voluptatibus aspernatur omnis nesciunt facere explicabo,
      necessitatibus odio, sit ex recusandae? Praesentium illo quo tenetur vel
      iure ipsa consectetur. reprehenderit. Ea architecto autem nemo voluptatem
      aliquam deleniti ducimus unde?
    </p>

    <h2 id = "s2">Section 2</h2>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Magni vel
      voluptas debitis. Ipsa architecto aspernatur quaerat praesentium magni.
      Perspiciatis saepe molestiae esse consequuntur dolorem exercitationem
      asperiores sit, eos odio, est repellat veritatis voluptate modi.
      Consequatur eos a quisquam quidem illum, labore aliquid sunt voluptas
      mollitia saepe animi voluptate iure cum ducimus quaerat autem optio iste
      suscipit tempore. Iure recusandae nam necessitatibus autem ipsa nihil
      velit, sapiente hic provident, quisquam dignissimos voluptatum sint
      deleniti magnam fuga ea enim. Quis rem perferendis perspiciatis molestiae
      molestias excepturi atque consectetur blanditiis! Dolorem voluptatum
      accusamus eaque ratione voluptatem quaerat atque dicta mollitia,
      laudantium beatae placeat quia quasi neque obcaecati quidem consequatur
      illum quae labore. Necessitatibus ducimus maxime velit asperiores in
      magni! Dolores eum debitis itaque? Lorem ipsum dolor sit amet consectetur
      adipisicing elit. Numquam, beatae quas! Asperiores fugit, deserunt
      dignissimos quam, quis quidem totam cupiditate expedita et molestias
      architecto nesciunt facere culpa accusantium id unde?Lorem ipsum dolor sit
      amet consectetur adipisicing elit. Labore explicabo ad id! Quo ullam,
      vitae expedita alias neque delectus pariatur vero aut excepturi beatae,
      dolore ducimus nulla cumque perspiciatis consequatur incidunt ipsum
      nostrum maiores quos quasi aspernatur fugiat maxime molestiae placeat.
      Sint quasi officiis ea magnam dicta cumque libero quam ad ullam
      reprehenderit et assumenda, rerum blanditiis consequatur obcaecati
      quisquam voluptate quae eum porro doloremque, hic ipsum! Qui fugit
      repellat nesciunt quidem quibusdam laboriosam fuga corrupti, vero rem
      tenetur veritatis. Nemo minima esse reiciendis, saepe excepturi ducimus
      qui voluptatum perferendis sequi corporis eum nostrum itaque sed adipisci,
      omnis fugit pariatur! Ab illum laboriosam explicabo molestiae architecto
      nihil doloribus ut nulla, eligendi dolorum maxime labore! Corporis harum
      vel nemo pariatur repellat ea, amet molestiae eaque illum aliquid
      voluptate voluptates voluptatem debitis magni cum architecto inventore
      velit alias exercitationem? Ad corrupti facilis cum magni nulla illum!
      Itaque aliquam maiores rerum ut praesentium consequuntur repellat aperiam
      deleniti, veniam laboriosam excepturi ullam iste adipisci beatae laborum
      et enim voluptatibus nisi autem dolorem laudantium nostrum doloremque
      odio. Dolorem nesciunt est aut inventore recusandae nobis suscipit ab
      maxime corporis dignissimos minus unde magnam, molestias error? Pariatur,
      quibusdam fugiat aperiam doloribus voluptate repellat saepe sed nam hic
      nesciunt quaerat vel laudantium culpa ad facere, earum odio impedit unde
      mollitia amet? Rem, at ut nemo, tempora, nobis numquam expedita veritatis
      voluptates eius dolores atque quibusdam minus nulla eaque accusamus
      reprehenderit itaque unde velit! Suscipit iusto obcaecati blanditiis
      dolores inventore, nemo ipsam sapiente sed qui voluptate laboriosam,
      aliquid maxime recusandae tenetur illo. Commodi illo distinctio ab
      accusantium maxime ipsum corporis, accusamus qui explicabo? Dolore,
      explicabo. Itaque facilis non magni minus error harum consectetur nemo
      architecto, eligendi maxime laboriosam voluptas neque nostrum delectus cum
      sapiente quaerat veniam nisi distinctio sit vitae aspernatur autem!
      Assumenda unde excepturi facilis nisi, iste atque ut dolor quos vero
      reiciendis voluptatum itaque iure sapiente iusto eaque ullam quis quas est
      laborum obcaecati aperiam cum ratione? Magnam sed nulla libero officia
      cupiditate voluptas consequatur! Fugit, provident molestias facere
      suscipit laborum aliquid repellendus voluptates tempora eos commodi dolore
      omnis odit et hic modi animi, dolorem obcaecati accusantium nihil eum
      delectus? Unde accusantium quasi magnam perspiciatis exercitationem
      cupiditate at molestiae doloribus, architecto illum corporis tempore
      dolores voluptas in explicabo culpa debitis alias, repudiandae natus?
      Provident cum rem ipsum. Ipsum odio dolorem eos id debitis repellendus
      placeat ratione tempore possimus voluptatibus error, ad deleniti
      perspiciatis vel cum quibusdam, voluptate, ipsam voluptates nam voluptas
      rem! Quo non expedita earum delectus temporibus, nostrum reiciendis alias
      commodi laboriosam optio iusto consectetur, sint culpa minus ea cupiditate
      distinctio voluptatem nisi deserunt! Illum eveniet quia aperiam dicta
      enim. Quia illo non at! Eaque vel repellat, unde minima rem temporibus
      sint quisquam, ipsum, modi ex blanditiis. Molestiae sit molestias ex
      animi, officia aut, excepturi porro rem pariatur, ipsam ea recusandae
      corporis quaerat alias dignissimos odit similique. Cum tenetur est neque
      sed quis aperiam sapiente possimus adipisci nam, magni repellendus minus
      id incidunt! Ipsa at tempore repellat incidunt tenetur quaerat provident!
      Reiciendis odio at itaque nam! Quidem modi, distinctio excepturi nam
      molestias quas, necessitatibus ad, iure error a nulla quae repellat ipsa
      aliquam. Unde voluptatibus distinctio impedit. Porro, provident
      repellendus ipsam voluptates veniam non laboriosam molestiae amet
      accusantium consequatur illo necessitatibus quo officiis sapiente eligendi
      rem iusto qui unde, illum, recusandae quod! Magnam eaque optio deserunt
      officia quibusdam magni cumque dolor atque placeat cum consectetur vel
      quam modi a voluptate obcaecati expedita, nulla itaque neque incidunt
      totam, perspiciatis dicta minus! Voluptas error blanditiis corrupti
      mollitia dolorem, illo dicta aliquid officiis tempora iste nulla facere,
      quo hic! Reprehenderit ea facere labore voluptates dolore accusamus
      ducimus placeat distinctio. Illum tempora labore obcaecati! Repudiandae,
      at maxime perspiciatis ex, totam maiores deserunt a quibusdam dolores
      cumque, cum facere! Esse nemo tempora impedit iure sapiente eligendi non
      excepturi, reiciendis praesentium autem a architecto alias maiores totam
      mollitia minima atque facilis quas! Perferendis vero corporis explicabo
      autem mollitia esse beatae dignissimos error cumque assumenda tenetur
      commodi, animi dolorem necessitatibus sapiente. Qui magnam adipisci
      inventore repellendus consequatur tempore eveniet unde. Doloribus, officia
      quasi et aperiam quidem sapiente asperiores iusto? Magnam, in sed?
      Provident atque omnis temporibus voluptate? Maxime nesciunt nisi debitis.
      Quo veniam corrupti itaque, vitae quae debitis? Adipisci ipsam voluptates
      dolores mollitia nesciunt reiciendis error provident laboriosam? Officia
      tempora alias numquam est asperiores modi veritatis et reiciendis nisi ut
      corporis quam, odit deserunt omnis odio ad iure maxime explicabo aut
      aliquam, rem adipisci exercitationem sunt! Fuga officiis, tempore,
      doloribus rerum esse alias dolores nam, cupiditate vero non aperiam
      praesentium perferendis ipsam voluptatem saepe exercitationem! Adipisci
      quaerat delectus, quia magni provident commodi in sint quod inventore
      explicabo! Repudiandae, veritatis dolorem obcaecati non possimus
      cupiditate eos dolorum veniam commodi dignissimos esse blanditiis repellat
      tempore impedit ex fugit incidunt autem, quo culpa minus! Quisquam
      reprehenderit error esse excepturi, similique tempora quas quis. Facere
      magnam quae earum hic numquam dignissimos quia exercitationem impedit
      blanditiis cum soluta deleniti nobis cumque suscipit possimus placeat
      iusto asperiores, perferendis fuga consectetur nesciunt ipsum fugit!
      Fugiat ea magnam impedit? Voluptatem sit dicta quam quas nobis reiciendis
      a commodi. Neque velit asperiores rerum, vel aliquid consequuntur itaque
      vero cumque adipisci, culpa assumenda quia a tenetur. Ad temporibus saepe
      dolore doloremque omnis suscipit quaerat dicta? Quasi molestiae totam
      reprehenderit facere error ipsum laborum quia veritatis suscipit.
      Praesentium pariatur dolores vitae dicta optio error, consectetur, ex
      earum obcaecati exercitationem est, facilis nesciunt perferendis odit unde
      quia corporis voluptates consequatur veniam recusandae ducimus eum ea
      nihil. Natus nostrum illo eaque veniam. Ex itaque esse tempore quam.
      Labore, excepturi vitae. Nobis totam minus officiis perspiciatis corrupti
      ipsa, nemo ipsum numquam in adipisci! Amet molestias doloribus velit ea,
      natus, sint optio dolores autem, earum nesciunt aliquid inventore
      pariatur? Eos perspiciatis error veritatis quod pariatur non quisquam,
      harum magnam saepe nihil soluta dolor laudantium, commodi eaque adipisci.
      Deleniti laudantium omnis, provident odio eius ad officiis consequuntur
      possimus id iusto sed velit! Ducimus dicta eius illo molestiae veniam
      esse. Magni, explicabo adipisci excepturi illo quo molestiae ullam iste.
      Eum alias, enim voluptatum beatae neque culpa ducimus repellendus dolore
      illum perspiciatis ipsa consequatur fuga necessitatibus exercitationem,
      rem minima, qui iure molestias nihil nulla explicabo cumque nemo esse
      deserunt? Dignissimos aperiam accusamus quae deleniti voluptate laboriosam
      iure officia adipisci, quaerat, commodi, amet ex nesciunt! Odio, aut
      inventore tempora repellat id quidem facere dolore dicta omnis amet
      praesentium esse ex vero a. Cum, ullam aliquam. Magnam debitis culpa
      adipisci nulla at similique sunt amet, asperiores repellendus eaque earum
      eius laborum facilis porro. Doloremque, iusto nostrum repellendus
      assumenda quaerat exercitationem eius nemo porro ratione molestiae,
      voluptas omnis, sint laudantium neque fugit nihil facere asperiores
      expedita cumque laboriosam quibusdam dolorem consectetur eveniet!
      Excepturi perspiciatis odit provident earum similique possimus a, esse
      voluptatum in, sint et modi, dolorum molestias quasi vitae ea blanditiis
      tempore quam soluta atque saepe. Necessitatibus, a. Nihil porro est
      quaerat suscipit omnis praesentium explicabo fugiat distinctio, quis et
      ipsum veniam ab animi illo dolore eum nostrum, unde nesciunt. Optio
      officia tempora natus unde, harum neque deserunt est nobis, reprehenderit
      praesentium illo iure cumque corrupti saepe asperiores! Harum sequi quos
      atque soluta mollitia tempora error veritatis, perspiciatis repellendus
      officiis illo quidem alias aut necessitatibus sit id eaque vero maxime.
      Iste quidem commodi error, aperiam cum incidunt sed nemo necessitatibus,
      hic omnis recusandae sequi est molestias? Iusto corrupti saepe in, tenetur
      suscipit magni aut voluptas nostrum ipsam voluptatum debitis neque, ex
      blanditiis quia non sunt totam odit, recusandae minus cupiditate! Earum
      nobis harum molestiae iure voluptas veniam minus ad assumenda ut quod
      tempore adipisci voluptatum cumque sequi, molestias quam eius ex non
      soluta aperiam fugit voluptate, eum est veritatis? Possimus voluptate
      porro atque aliquid est deleniti voluptates odit provident ratione veniam
      consequuntur ex ipsum dolore, dolorum illum hic similique fugit sed
      doloribus dicta doloremque sint labore explicabo. Hic, consequuntur ipsum!
      Ducimus minima quia dicta maiores ea quis, in suscipit magni animi
      laudantium mollitia excepturi recusandae soluta rerum consequatur,
      eligendi obcaecati officia? Quibusdam ipsam ab, numquam enim molestias
      perferendis assumenda in ea ad eos at, nobis pariatur facere eum odit
      minima! Eaque, dolor eos voluptas excepturi harum dicta magni aspernatur
      consequatur deserunt rerum dolorum illum, nihil ad pariatur quidem nostrum
      sunt. Distinctio assumenda dolorum, soluta veritatis explicabo accusantium
      mollitia! Ratione dolores molestias vitae? Libero fuga ut possimus nobis
      magnam voluptates distinctio? Facere illo illum natus doloremque est
      dolorem saepe, molestias quaerat aspernatur sapiente? Nihil maxime iste
      placeat id voluptatem possimus eum doloremque ipsum aperiam rem, quo
      quidem voluptatibus sint quae cum dolorem, culpa nemo. Tempora veniam
      facilis provident nisi officiis, iure, dolore vero porro distinctio quam
      asperiores modi consequatur eveniet quod, velit accusamus minus ea. Sunt
      illum quo ullam consequuntur, sequi quia quidem repellat rem sed
      dignissimos accusamus assumenda vel libero esse odit natus nihil itaque.
      Beatae quibusdam earum, nulla odit eveniet aperiam libero esse tempore?
      Ullam recusandae, maiores quaerat id dolores nobis? Exercitationem
      molestias voluptatem nemo, itaque minus quam et ullam illo nihil quod
      amet, debitis magnam vitae sed. Quos delectus quam est reiciendis tempore,
      non, magni magnam laudantium aliquam sequi quis blanditiis nobis quibusdam
      repellendus quia deleniti tempora nesciunt expedita velit natus
      perferendis iure ipsum quae! At ut fugiat debitis exercitationem ducimus
      voluptatibus vero provident! Nesciunt, adipisci! Nisi minima laudantium
      quisquam, nostrum temporibus harum laboriosam velit ea non ut architecto?
      Culpa maxime quia possimus quibusdam accusamus impedit beatae quis nisi a
      atque consequuntur deleniti, distinctio neque? Nulla consectetur quibusdam
      quos odio accusantium rerum ut sapiente voluptatum aliquid tempora itaque
      debitis exercitationem voluptates dolor quaerat, explicabo facere nostrum
      obcaecati delectus neque. Nemo, aliquam corrupti optio in ea nulla vel,
      ducimus, nobis hic veritatis temporibus? Excepturi laborum placeat
      explicabo iusto eos porro nihil optio inventore iste, quis, facere eius
      deserunt vel ab facilis culpa neque in veritatis omnis! Consectetur
      aliquam inventore natus facere sequi quo excepturi et optio sint soluta!
      Odit corrupti asperiores cupiditate possimus odio tempora libero animi
      labore quia? Inventore quaerat aut sunt recusandae adipisci dolores eius
      alias voluptas non numquam molestias placeat maxime repellendus,
      architecto rerum blanditiis harum. Fugit labore blanditiis quam, delectus
      voluptas similique nulla doloremque maxime sit est eligendi pariatur
      voluptate ducimus non earum qui consequatur libero! Adipisci quia nam
      velit consequuntur omnis, at molestias obcaecati doloremque sit, quos
      voluptatem ut nesciunt illo! Porro tempora aliquid veniam, unde
      consequuntur debitis quaerat. Eaque ea est atque dolor dolorem nobis minus
      nesciunt porro, animi quia nulla dignissimos. Incidunt delectus itaque
      doloremque eius earum placeat distinctio cupiditate modi ut sit. Dolor, a
      at. Distinctio recusandae tempora ex eligendi dolores? Quam, a unde eos,
      cupiditate ratione magnam, sapiente praesentium reiciendis inventore ullam
      totam commodi veritatis ut. Ipsum dolor ipsa ex aliquid, id rem itaque
      quod saepe explicabo autem! Cupiditate aspernatur illo veritatis, ex
      provident natus tempore est? Aliquid quod magnam maxime harum nihil optio
      facere ut sed, sapiente enim. Rerum quam quaerat odio perferendis modi cum
      earum qui provident repudiandae assumenda laudantium ratione dignissimos,
      animi possimus obcaecati aperiam? Alias consequuntur rerum ipsa porro
      minus mollitia deserunt dicta nostrum accusantium doloremque quia magnam
      repellendus odit saepe at reprehenderit molestiae earum iusto, illum
      totam! Nostrum minus reprehenderit culpa veritatis officiis asperiores
      placeat! Ducimus et excepturi, impedit error illo repudiandae assumenda
      quo. Odit nisi perferendis mollitia magnam hic, repudiandae soluta
      inventore nemo, modi dolore accusamus! Accusamus, possimus quia eligendi
      esse officiis minima sequi, minus voluptatem quod corporis architecto
      dolor aspernatur dolorem optio nihil similique voluptas deleniti, non
      recusandae assumenda fuga quo illo sit impedit. Fugiat quae delectus
      aliquam suscipit nulla obcaecati numquam consectetur id temporibus, ipsa
      consequatur molestias alias eos corrupti autem facere repellat voluptates.
      Id aspernatur, possimus repudiandae dignissimos at cumque, similique
      molestiae quaerat velit et fugit vitae magnam dolorum fugiat. Eaque rem,
      neque provident eius earum, ab, laboriosam non quas nam unde consectetur
      tempora tenetur facilis aut rerum ad magni? Provident modi consequatur
      ducimus quisquam, eius iusto non quod, soluta hic, commodi doloribus
      incidunt in sit sint culpa voluptate aut assumenda debitis autem deleniti?
      Quia quam qui ipsam id perspiciatis sequi fugiat provident beatae
      consequatur recusandae consectetur nisi doloribus magnam necessitatibus
      autem odio commodi, dolores nulla adipisci. Magni eius dicta, repellat
      laboriosam, esse velit molestias eaque aliquid dolore harum neque,
      dignissimos maiores perferendis dolorum? psa eos quos deserunt, reiciendis
      dolor omnis sequi minus, aut, necessitatibus magni corrupti. Qui quis
      reprehenderit, error quod, nobis non aperiam autem, praesentium modi et
      deserunt quia repellat natus recusandae maxime magnam ea delectus
      asperiores voluptates sit dignissimos vero libero. Necessitatibus, dolore
      quod dolorum excepturi minima voluptatum asperiores quae cum. Dicta
      voluptatibus debitis maxime! Voluptatum fuga id accusantium natus hic
      ducimus aperiam quis provident ratione quo. Deserunt molestiae corrupti
      natus suscipit non vero debitis enim, odio accusantium similique sapiente
      dolor maxime optio a doloribus eius est repudiandae accusamus cumque
      aspernatur? Porro ipsum officia recusandae quas aspernatur at iste veniam.
      Rerum ullam libero mollitia quos accusantium dignissimos voluptatum! Nihil
      vitae recusandae qui quos nemo, officia laudantium ex, alias debitis
      inventore repudiandae itaque similique? Architecto ipsam ea tempore
      similique corrupti qui placeat necessitatibus esse blanditiis expedita
      officiis quos, vero sint nobis obcaecati doloribus rerum a! Repellat
      delectus voluptatum laboriosam, maiores hic dolorum accusantium veniam
      omnis dolore ullam! Ad doloribus temporibus soluta, quos, cupiditate
      accusantium ipsam in sapiente labore eos eum hic ex? Odio repudiandae
      voluptatum blanditiis et quos, aperiam, ea nisi culpa qui fugit sint cum
      quasi! Facere tenetur qui, asperiores ipsam similique rerum quae tempore,
      laborum repudiandae quibusdam praesentium saepe a iure impedit, culpa eos
      corrupti vitae dicta. Libero facilis consequatur, labore quisquam illum
      rem quia consectetur earum veritatis accusantium officia quae tempora aut
      voluptatibus sed porro maiores ab velit? Veritatis error at quas iusto
      ducimus id tenetur, dolorum illo tempore dolor quod, explicabo, beatae
      temporibus iure suscipit odit. Ex consequatur impedit possimus natus qui
      totam quam incidunt. Blanditiis ratione quos quasi hic ab veniam itaque
      fuga saepe similique eaque ullam tenetur distinctio, enim, alias quia amet
      temporibus dicta, consequuntur mollitia.
    </p>

    <h2 id = "s3">Section 3</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero, animi
      eos. Dolores porro dolore, nulla maiores reprehenderit neque, culpa, eaque
      quos minus iusto ducimus autem ex consequatur. Minus, maxime atque
      exercitationem excepturi, soluta facilis quidem doloribus, impedit earum
      molestias molestiae voluptatem voluptatibus odio. Asperiores suscipit eos
      non maiores. Atque aspernatur quidem omnis, aut aperiam id perferendis
      incidunt cum! Veritatis, aut nostrum quisquam quae nobis unde? Sint quos
      illo facilis ex ab! Officiis enim aut nihil laborum adipisci alias a qui,
      debitis, nulla recusandae repudiandae numquam aliquam labore sequi vitae
      fugiat inventore. Laborum nam, eius veritatis nulla voluptas aperiam odit
      fugiat repellendus ab est. Sed repellat corporis vitae unde eligendi
      deleniti quae distinctio similique commodi eum, accusantium illum sint
      modi reiciendis error, provident, magni voluptatem veniam quod. Quae
      labore laboriosam repudiandae accusantium voluptatibus. Quaerat, ducimus
      qui! Vel temporibus dolore dolorum quos magnam, non, aperiam quam,
      pariatur provident possimus assumenda laboriosam! Quas illo quam dolorum
      reprehenderit exercitationem veniam voluptate, libero esse, earum eum
      saepe explicabo voluptas cum recusandae repellendus fugit praesentium odio
      odit maiores obcaecati a accusantium neque veritatis temporibus! Dolorum
      neque voluptas qui suscipit sunt tenetur excepturi unde eligendi
      necessitatibus molestiae quo eum, dolore repudiandae, harum vitae
      laboriosam iste? Obcaecati aspernatur aut minus nobis. Nostrum, sunt
      incidunt nulla, quisquam, a iusto corporis impedit tempora repudiandae
      obcaecati accusamus quaerat dolores perferendis quia veritatis vero harum
      quidem provident ut architecto ab hic iste quos. At nesciunt tenetur odit
      aut hic tempora magnam doloribus suscipit quae possimus consequuntur ipsum
      adipisci vero, rerum, explicabo sit? Accusantium delectus laborum
      repudiandae corrupti, incidunt iusto voluptates et omnis? Eaque fuga
      consectetur magni ex nostrum illo cupiditate vitae quod, architecto, hic
      eligendi laborum, quae pariatur alias molestias repellendus quis nesciunt
      autem? Aliquid, quaerat voluptatum quae porro nostrum, eveniet
      necessitatibus facere placeat, perferendis nemo ullam quo officia harum
      dignissimos? Odio, possimus ullam! Unde enim debitis, vero voluptatum,
      iusto, iste consequatur exercitationem natus sequi et doloribus. Repellat
      tenetur hic autem excepturi iste eligendi laborum temporibus dolore,
      quibusdam dicta asperiores itaque sed cumque eum dolor sunt? Molestias
      quaerat aliquid, eligendi inventore, hic veniam maiores quasi, minima
      quibusdam dolorum quidem facere. Consequuntur quidem repellat numquam
      ratione nesciunt voluptatum, qui, sapiente placeat nihil, dolorem culpa
      beatae alias neque. At quia, magnam itaque obcaecati amet aspernatur
      maxime hic nihil omnis adipisci mollitia harum veritatis, voluptate totam
      voluptas, quas perspiciatis fugit unde. Quaerat quos eius, amet ea quam
      maiores consectetur perferendis ipsam animi aut, molestiae iure!
    </p>
    <script>
      // Q Implement key taps such that on pressing 1 you scroll to section 1,  pressing 2 you scroll to section 2 and  pressing 3 you scroll to section 3. Also implement key tap b to go to bottom of the page and key tap t to go to top of the page

      let s1 = document.querySelector("#s1");
      let s2 = document.querySelector("#s2");
      let s3 = document.querySelector("#s3");

      document.addEventListener("keydown", function (e) {
        //  console.log(e.key)

        if (e.key == 1) {
          s1.scrollIntoView();
        } else if (e.key == 2) {
          s2.scrollIntoView();
        } else if (e.key == 3) {
          s3.scrollIntoView();
        } else if (e.key == "b") {
          window.scrollBy(
            0,
            document.querySelector("html").getBoundingClientRect().height
          );
        } else if (e.key == "t") {
          window.scrollBy(
            0,
            -document.querySelector("html").getBoundingClientRect().height
          );
        }
      });
    </script>
  </body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/282/original/upload_256151d33674a1879c7f92d29007cc30.png?1695147949)

---
title: getBoundingClientRect() Method
description:
duration: 900
card_type: cue_card
---

#### Question 3

How to retrive position and dimensions of an element usng getBoundingClientRect() method?

**getBoundingClientRect():** The `getBoundingClientRect()` method is a JavaScript method that is used to retrieve the position and dimensions of an element relative to the viewport (the visible area of a web page). It returns a DOMRect object containing properties like top, left, right, bottom, width, and height, which describe the position and size of the element. 

#### Solution

```javascript
<!DOCTYPE html>
<html lang = "en">
  <head>
    <meta charset = "UTF-8" />
    <meta http - equiv = "X - UA - Compatible" content = "IE = edge" />
    <meta name = "viewport" content = "width = device - width, initial - scale = 1.0" />
    <title>Document</title>

    <style>
      #hello {
        height: 100px;
        width: 150px;
        position: absolute;
        top: 20px;
        left: 100px;
      }
    </style>
  </head>
  <body>
    <div id = "hello">Hello</div>

    <script>
      let helloDiv = document.querySelector("#hello");

      const results = helloDiv.getBoundingClientRect();
      console.log(results);
    </script>
  </body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/283/original/upload_da6af4f47c894b96f06c245049c1a675.png?1695148027)


---
title: Button working
description:
duration: 900
card_type: cue_card
---

#### Question 4

Make remove all button work  and make individual delete btn work
 
#### Solution

```javascript
<!DOCTYPE html>
<html lang = "en">
  <head>
    <meta charset = "UTF - 8" />
    <meta http-equiv = "X - UA - Compatible" content = "IE = edge" />
    <meta name = "viewport" content = "width = device - width, initial-scale = 1.0" />
    <title>Document</title>
  </head>
  <body>
    <button id = "removeAll">Remove All</button>
    <ul>
      <li>
        <p>Task - 1</p>
        <button class="delete_button">delete</button>
      </li>
      <li>
        <p>Task - 2</p>
        <button class="delete_button">delete</button>
      </li>
      <li>
        <p>Task - 3</p>
        <button class="delete_button">delete</button>
      </li>
      <li>
        <p>Task - 4</p>
        <button class="delete_button">delete</button>
      </li>
    </ul>
    <script>
      // Q- Make remove all button work  and make individual delete btn work
      //   Solution:

      let removeAllBtn = document.querySelector("#removeAll");

      let ul = document.querySelector("ul");

      let AllDeleteButton = document.querySelectorAll(".delete_button");

      let AllListItems = ul.querySelectorAll("li");

      for (let i = 0; i < AllDeleteButton.length; i ++ ) {
        AllDeleteButton[i].addEventListener("click", function (e) {
          e.currentTarget.parentElement.remove();
        });
      }

      removeAllBtn.addEventListener("click", function () {
        AllListItems = ul.querySelectorAll("li");

        for (let i = 0; i < AllListItems.length; i ++ ) {
          ul.removeChild(AllListItems[i]);
        }
      });
    </script>
  </body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/285/original/upload_ce32e1b3379121858f8ccc0ec9bb1268.png?1695148118)



#### Question 5

Create a button that is destroyed by clicking on it but two new buttons are created in it's place.
 
#### Solution

```javascript
<!DOCTYPE html>
<html lang = "en">
  <head>
    <meta charset = "UTF - 8" />
    <meta http-equiv = "X - UA - Compatible" content = "IE = edge" />
    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0" />
    <title>Document</title>
  </head>
  <body>
    <div id = "doubleHolder">
      <button class = "double">double</button>
    </div>

    <script>
      //    Q Create a button that is destroyed by clicking on it but two new buttons are created in it's place.

      //   Solution:

      document
        .querySelector("#doubleHolder")
        .addEventListener("click", function (e) {
          if (e.target.classList.contains("double")) {
            let btn = document.createElement("button");
            btn.setAttribute("class", "triple");
            btn.innerHTML = "Double";

            let btn2 = document.createElement("button");
            btn2.setAttribute("class", "triple");
            btn2.innerHTML = "Double";

            e.currentTarget.appendChild(btn);
            e.currentTarget.appendChild(btn2);

            e.currentTarget.removeChild(e.target);
          }
        });
    </script>
  </body>
</html>

```

**Output:**

![](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/049/286/original/upload_41220be67c87ecd8f41c99e72309656a.png?1695148181)
