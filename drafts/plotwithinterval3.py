import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
from matplotlib import ticker

# Vos données
data = [[1714454618.979, "0.034290239258011966"], [1714454619.979, "0.035778718446508526"], [1714454620.979, "0.035778718446508526"], [1714454621.979, "0.035778718446508526"], [1714454622.979, "0.035778718446508526"], [1714454623.979, "0.035778718446508526"], [1714454624.979, "0.035778718446508526"], [1714454625.979, "0.035778718446508526"], [1714454626.979, "0.03622265478084649"], [1714454627.979, "0.03622265478084649"], [1714454628.979, "0.03622265478084649"], [1714454629.979, "0.03622265478084649"], [1714454630.979, "0.03622265478084649"], [1714454631.979, "0.03622265478084649"], [1714454632.979, "0.03622265478084649"], [1714454633.979, "0.03622265478084649"], [1714454634.979, "0.03622265478084649"], [1714454635.979, "0.04204108405911944"], [1714454636.979, "0.04204108405911944"], [1714454637.979, "0.04204108405911944"], [1714454638.979, "0.04204108405911944"], [1714454639.979, "0.04204108405911944"], [1714454640.979, "0.04204108405911944"], [1714454641.979, "0.04204108405911944"], [1714454642.979, "0.04204108405911944"], [1714454643.979, "0.04204108405911944"], [1714454644.979, "0.04204108405911944"], [1714454645.979, "0.0431620849130584"], [1714454646.979, "0.0431620849130584"], [1714454647.979, "0.0431620849130584"], [1714454648.979, "0.0431620849130584"], [1714454649.979, "0.0431620849130584"], [1714454650.979, "0.0431620849130584"], [1714454651.979, "0.0431620849130584"], [1714454652.979, "0.0431620849130584"], [1714454653.979, "0.0431620849130584"], [1714454654.979, "0.04499850103246576"], [1714454655.979, "0.04499850103246576"], [1714454656.979, "0.04499850103246576"], [1714454657.979, "0.05000980780825923"], [1714454658.979, "0.05000980780825923"], [1714454659.979, "0.05000980780825923"], [1714454660.979, "0.05000980780825923"], [1714454661.979, "0.05000980780825923"], [1714454662.979, "0.05000980780825923"], [1714454663.979, "0.05000980780825923"], [1714454664.979, "0.05000980780825923"], [1714454665.979, "0.04132538251164087"], [1714454666.979, "0.04132538251164087"], [1714454667.979, "0.04132538251164087"], [1714454668.979, "0.04132538251164087"], [1714454669.979, "0.04132538251164087"], [1714454670.979, "0.031200826224160455"], [1714454671.979, "0.031200826224160455"], [1714454672.979, "0.031200826224160455"], [1714454673.979, "0.031200826224160455"], [1714454674.979, "0.031200826224160455"], [1714454675.979, "0.031200826224160455"], [1714454676.979, "0.031200826224160455"], [1714454677.979, "0.031200826224160455"], [1714454678.979, "0.031200826224160455"], [1714454679.979, "0.031200826224160455"], [1714454680.979, "0.031200826224160455"], [1714454681.979, "0.031200826224160455"], [1714454682.979, "0.031200826224160455"], [1714454683.979, "0.031200826224160455"], [1714454684.979, "0.03470400505564661"], [1714454685.979, "0.03470400505564661"], [1714454686.979, "0.03470400505564661"], [1714454687.979, "0.03470400505564661"], [1714454688.979, "0.03911642582887877"], [1714454689.979, "0.03911642582887877"], [1714454690.979, "0.03911642582887877"], [1714454691.979, "0.03911642582887877"], [1714454692.979, "0.03911642582887877"], [1714454693.979, "0.03911642582887877"], [1714454694.979, "0.03911642582887877"], [1714454695.979, "0.03911642582887877"], [1714454696.979, "0.03911642582887877"], [1714454697.979, "0.03911642582887877"], [1714454698.979, "0.03911642582887877"], [1714454699.979, "0.03911642582887877"], [1714454700.979, "0.03911642582887877"], [1714454701.979, "0.03911642582887877"], [1714454702.979, "0.03911642582887877"], [1714454703.979, "0.035793569565111275"], [1714454704.979, "0.03278327946358817"], [1714454705.979, "0.03278327946358817"], [1714454706.979, "0.03278327946358817"], [1714454707.979, "0.03278327946358817"], [1714454708.979, "0.03278327946358817"], [1714454709.979, "0.03278327946358817"], [1714454710.979, "0.03278327946358817"], [1714454711.979, "0.03278327946358817"], [1714454712.979, "0.03278327946358817"], [1714454713.979, "0.03278327946358817"], [1714454714.979, "0.03278327946358817"], [1714454715.979, "0.03278327946358817"], [1714454716.979, "0.03278327946358817"], [1714454717.979, "0.03278327946358817"], [1714454718.979, "0.03278327946358817"], [1714454719.979, "0.4930472678390384"], [1714454720.979, "0.4930472678390384"], [1714454721.979, "0.9271282579087635"], [1714454722.979, "0.9271282579087635"], [1714454723.979, "0.9271282579087635"], [1714454724.979, "0.9271282579087635"], [1714454725.979, "0.9271282579087635"], [1714454726.979, "0.9271282579087635"], [1714454727.979, "0.9271282579087635"], [1714454728.979, "0.9271282579087635"], [1714454729.979, "0.9271282579087635"], [1714454730.979, "0.9271282579087635"], [1714454731.979, "0.9271282579087635"], [1714454732.979, "0.581367659695613"], [1714454733.979, "0.581367659695613"], [1714454734.979, "0.581367659695613"], [1714454735.979, "0.3078581551466989"], [1714454736.979, "0.3078581551466989"], [1714454737.979, "0.3078581551466989"], [1714454738.979, "0.3078581551466989"], [1714454739.979, "0.3078581551466989"], [1714454740.979, "0.3078581551466989"], [1714454741.979, "0.3078581551466989"], [1714454742.979, "0.3078581551466989"], [1714454743.979, "0.3078581551466989"], [1714454744.979, "0.3078581551466989"], [1714454745.979, "0.3221718363296024"], [1714454746.979, "0.3221718363296024"], [1714454747.979, "0.3221718363296024"], [1714454748.979, "0.3221718363296024"], [1714454749.979, "0.3221718363296024"], [1714454750.979, "0.3221718363296024"], [1714454751.979, "0.3221718363296024"], [1714454752.979, "0.3221718363296024"], [1714454753.979, "0.3221718363296024"], [1714454754.979, "0.3221718363296024"], [1714454755.979, "0.3221718363296024"], [1714454756.979, "0.3221718363296024"], [1714454757.979, "0.3221718363296024"], [1714454758.979, "0.3221718363296024"], [1714454759.979, "0.3221718363296024"], [1714454760.979, "0.22690331607468128"], [1714454761.979, "0.22690331607468128"], [1714454762.979, "0.22690331607468128"], [1714454763.979, "0.22690331607468128"], [1714454764.979, "0.061522833340016445"], [1714454765.979, "0.061522833340016445"], [1714454766.979, "0.061522833340016445"], [1714454767.979, "0.061522833340016445"], [1714454768.979, "0.061522833340016445"], [1714454769.979, "0.061522833340016445"], [1714454770.979, "0.061522833340016445"], [1714454771.979, "0.061522833340016445"], [1714454772.979, "0.061522833340016445"], [1714454773.979, "0.19623449896580267"], [1714454774.979, "0.19623449896580267"], [1714454775.979, "0.19623449896580267"], [1714454776.979, "0.19623449896580267"], [1714454777.979, "0.19623449896580267"], [1714454778.979, "0.19623449896580267"], [1714454779.979, "0.19623449896580267"], [1714454780.979, "0.32146688005945323"], [1714454781.979, "0.32146688005945323"], [1714454782.979, "0.32146688005945323"], [1714454783.979, "0.32146688005945323"], [1714454784.979, "0.32146688005945323"], [1714454785.979, "0.32146688005945323"], [1714454786.979, "0.32146688005945323"], [1714454787.979, "0.32146688005945323"], [1714454788.979, "0.32146688005945323"], [1714454789.979, "0.22697094211055294"], [1714454790.979, "0.22697094211055294"], [1714454791.979, "0.22697094211055294"], [1714454792.979, "0.22697094211055294"], [1714454793.979, "0.09170841826559412"], [1714454794.979, "0.09170841826559412"], [1714454795.979, "0.09170841826559412"], [1714454796.979, "0.09170841826559412"], [1714454797.979, "0.09170841826559412"], [1714454798.979, "0.09170841826559412"], [1714454799.979, "0.09170841826559412"], [1714454800.979, "0.09170841826559412"], [1714454801.979, "0.09170841826559412"], [1714454802.979, "0.09170841826559412"], [1714454803.979, "0.09170841826559412"], [1714454804.979, "0.09170841826559412"], [1714454805.979, "0.09170841826559412"], [1714454806.979, "0.04487458397010323"], [1714454807.979, "0.04487458397010323"], [1714454808.979, "0.04487458397010323"], [1714454809.979, "0.03333623120319414"], [1714454810.979, "0.03333623120319414"], [1714454811.979, "0.03333623120319414"], [1714454812.979, "0.03333623120319414"], [1714454813.979, "0.03333623120319414"], [1714454814.979, "0.03333623120319414"], [1714454815.979, "0.03333623120319414"], [1714454816.979, "0.03333623120319414"], [1714454817.979, "0.03333623120319414"], [1714454818.979, "0.05334260921342043"], [1714454819.979, "0.05334260921342043"], [1714454820.979, "0.05334260921342043"], [1714454821.979, "0.05334260921342043"], [1714454822.979, "0.05334260921342043"], [1714454823.979, "0.07530691680079521"], [1714454824.979, "0.07530691680079521"], [1714454825.979, "0.07530691680079521"], [1714454826.979, "0.07530691680079521"], [1714454827.979, "0.07530691680079521"], [1714454828.979, "0.07530691680079521"], [1714454829.979, "0.07530691680079521"], [1714454830.979, "0.07530691680079521"], [1714454831.979, "0.07530691680079521"], [1714454832.979, "0.07530691680079521"], [1714454833.979, "0.07530691680079521"], [1714454834.979, "0.07530691680079521"], [1714454835.979, "0.07530691680079521"], [1714454836.979, "0.07530691680079521"], [1714454837.979, "0.07530691680079521"], [1714454838.979, "0.07530691680079521"], [1714454839.979, "0.07530691680079521"], [1714454840.979, "0.07530691680079521"], [1714454841.979, "0.057344730707447264"], [1714454842.979, "0.057344730707447264"], [1714454843.979, "0.057344730707447264"], [1714454844.979, "0.057344730707447264"], [1714454845.979, "0.057344730707447264"], [1714454846.979, "0.057344730707447264"], [1714454847.979, "0.057344730707447264"], [1714454848.979, "0.057344730707447264"], [1714454849.979, "0.057344730707447264"], [1714454850.979, "0.057344730707447264"], [1714454851.979, "0.057344730707447264"], [1714454852.979, "0.057344730707447264"], [1714454853.979, "0.06994435296482569"], [1714454854.979, "0.06994435296482569"], [1714454855.979, "0.05503779717817843"], [1714454856.979, "0.05503779717817843"], [1714454857.979, "0.05503779717817843"], [1714454858.979, "0.05503779717817843"], [1714454859.979, "0.05503779717817843"], [1714454860.979, "0.05503779717817843"], [1714454861.979, "0.05503779717817843"], [1714454862.979, "0.05503779717817843"], [1714454863.979, "0.05503779717817843"], [1714454864.979, "0.05503779717817843"], [1714454865.979, "0.05503779717817843"], [1714454866.979, "0.11257510019028702"], [1714454867.979, "0.11257510019028702"], [1714454868.979, "0.11257510019028702"], [1714454869.979, "0.11257510019028702"], [1714454870.979, "0.11257510019028702"], [1714454871.979, "0.11257510019028702"], [1714454872.979, "0.11257510019028702"], [1714454873.979, "0.11257510019028702"], [1714454874.979, "0.11257510019028702"], [1714454875.979, "0.11257510019028702"], [1714454876.979, "0.11257510019028702"], [1714454877.979, "0.11257510019028702"], [1714454878.979, "0.07070192746254982"], [1714454879.979, "0.07070192746254982"], [1714454880.979, "0.07070192746254982"], [1714454881.979, "0.07070192746254982"], [1714454882.979, "0.07070192746254982"], [1714454883.979, "0.07070192746254982"], [1714454884.979, "0.07070192746254982"], [1714454885.979, "0.03475339713181128"], [1714454886.979, "0.03475339713181128"], [1714454887.979, "0.03475339713181128"], [1714454888.979, "0.03475339713181128"], [1714454889.979, "0.03475339713181128"], [1714454890.979, "0.03475339713181128"], [1714454891.979, "0.03475339713181128"], [1714454892.979, "0.03475339713181128"], [1714454893.979, "0.03475339713181128"], [1714454894.979, "0.03475339713181128"], [1714454895.979, "0.03475339713181128"], [1714454896.979, "0.03475339713181128"], [1714454897.979, "0.03475339713181128"], [1714454898.979, "0.10054515639254075"], [1714454899.979, "0.10054515639254075"], [1714454900.979, "0.10054515639254075"], [1714454901.979, "0.10054515639254075"], [1714454902.979, "0.10054515639254075"], [1714454903.979, "0.10054515639254075"], [1714454904.979, "0.1697424999655252"], [1714454905.979, "0.1697424999655252"], [1714454906.979, "0.1697424999655252"], [1714454907.979, "0.1697424999655252"], [1714454908.979, "0.1697424999655252"], [1714454909.979, "0.1697424999655252"], [1714454910.979, "0.1697424999655252"], [1714454911.979, "0.1697424999655252"], [1714454912.979, "0.1697424999655252"], [1714454913.979, "0.1697424999655252"], [1714454914.979, "0.1697424999655252"], [1714454915.979, "0.1697424999655252"], [1714454916.979, "0.10203512264237996"], [1714454917.979, "0.10203512264237996"], [1714454918.979, "0.10203512264237996"], [1714454919.979, "0.10203512264237996"], [1714454920.979, "0.10203512264237996"], [1714454921.979, "0.10203512264237996"], [1714454922.979, "0.10203512264237996"], [1714454923.979, "0.03149468334681003"], [1714454924.979, "0.03149468334681003"], [1714454925.979, "0.03149468334681003"], [1714454926.979, "0.03149468334681003"], [1714454927.979, "0.03149468334681003"], [1714454928.979, "0.03149468334681003"], [1714454929.979, "0.03149468334681003"], [1714454930.979, "0.03149468334681003"], [1714454931.979, "0.03149468334681003"], [1714454932.979, "0.03149468334681003"], [1714454933.979, "0.03149468334681003"], [1714454934.979, "0.03149468334681003"], [1714454935.979, "0.03149468334681003"], [1714454936.979, "0.03149468334681003"], [1714454937.979, "0.03149468334681003"], [1714454938.979, "0.03149468334681003"], [1714454939.979, "0.03149468334681003"], [1714454940.979, "0.03149468334681003"], [1714454941.979, "0.03149468334681003"], [1714454942.979, "0.03149468334681003"], [1714454943.979, "0.03149468334681003"], [1714454944.979, "0.033728931933007536"], [1714454945.979, "0.033728931933007536"], [1714454946.979, "0.03396403439959292"], [1714454947.979, "0.03396403439959292"], [1714454948.979, "0.03396403439959292"], [1714454949.979, "0.03396403439959292"], [1714454950.979, "0.03396403439959292"], [1714454951.979, "0.03396403439959292"], [1714454952.979, "0.03396403439959292"], [1714454953.979, "0.03396403439959292"], [1714454954.979, "0.03396403439959292"], [1714454955.979, "0.03396403439959292"], [1714454956.979, "0.031665932419251655"], [1714454957.979, "0.03166984020605044"], [1714454958.979, "0.03166984020605044"], [1714454959.979, "0.03166984020605044"], [1714454960.979, "0.03166984020605044"], [1714454961.979, "0.03166984020605044"], [1714454962.979, "0.03166984020605044"], [1714454963.979, "0.03166984020605044"], [1714454964.979, "0.03166984020605044"], [1714454965.979, "0.03166984020605044"], [1714454966.979, "0.03166984020605044"], [1714454967.979, "0.03139168750285683"], [1714454968.979, "0.032191485923641794"], [1714454969.979, "0.032191485923641794"], [1714454970.979, "0.032191485923641794"], [1714454971.979, "0.032191485923641794"], [1714454972.979, "0.032191485923641794"], [1714454973.979, "0.032191485923641794"], [1714454974.979, "0.032191485923641794"], [1714454975.979, "0.032191485923641794"], [1714454976.979, "0.032191485923641794"], [1714454977.979, "0.032191485923641794"], [1714454978.979, "0.032191485923641794"], [1714454979.979, "0.032191485923641794"], [1714454980.979, "0.03225883699047595"], [1714454981.979, "0.03225883699047595"], [1714454982.979, "0.03225883699047595"], [1714454983.979, "0.03386476724483585"], [1714454984.979, "0.03386476724483585"], [1714454985.979, "0.03386476724483585"], [1714454986.979, "0.03386476724483585"], [1714454987.979, "0.03386476724483585"], [1714454988.979, "0.03386476724483585"], [1714454989.979, "0.03386476724483585"], [1714454990.979, "0.03386476724483585"], [1714454991.979, "0.03386476724483585"], [1714454992.979, "0.03386476724483585"], [1714454993.979, "0.03386476724483585"], [1714454994.979, "0.03386476724483585"], [1714454995.979, "0.0359278457094285"], [1714454996.979, "0.0359278457094285"], [1714454997.979, "0.0359278457094285"], [1714454998.979, "0.0359278457094285"], [1714454999.979, "0.0359278457094285"], [1714455000.979, "0.03708631927378556"], [1714455001.979, "0.03708631927378556"], [1714455002.979, "0.03708631927378556"], [1714455003.979, "0.03708631927378556"], [1714455004.979, "0.03708631927378556"], [1714455005.979, "0.03708631927378556"], [1714455006.979, "0.03708631927378556"], [1714455007.979, "0.03708631927378556"], [1714455008.979, "0.03708631927378556"], [1714455009.979, "0.03708631927378556"], [1714455010.979, "0.03708631927378556"], [1714455011.979, "0.03708631927378556"], [1714455012.979, "0.03708631927378556"], [1714455013.979, "0.03708631927378556"], [1714455014.979, "0.04336150760409459"], [1714455015.979, "0.04336150760409459"], [1714455016.979, "0.04336150760409459"], [1714455017.979, "0.04336150760409459"], [1714455018.979, "0.04336150760409459"], [1714455019.979, "0.04336150760409459"], [1714455020.979, "0.048355420252436235"], [1714455021.979, "0.048355420252436235"], [1714455022.979, "0.048355420252436235"], [1714455023.979, "0.048355420252436235"], [1714455024.979, "0.048355420252436235"], [1714455025.979, "0.048355420252436235"], [1714455026.979, "0.048355420252436235"], [1714455027.979, "0.04317014641573068"], [1714455028.979, "0.04317014641573068"], [1714455029.979, "0.04317014641573068"], [1714455030.979, "0.04317014641573068"], [1714455031.979, "0.04317014641573068"], [1714455032.979, "0.04317014641573068"], [1714455033.979, "0.04317014641573068"], [1714455034.979, "0.04317014641573068"], [1714455035.979, "0.04317014641573068"], [1714455036.979, "0.04317014641573068"], [1714455037.979, "0.054410482741556604"], [1714455038.979, "0.054410482741556604"], [1714455039.979, "0.054410482741556604"], [1714455040.979, "0.054410482741556604"], [1714455041.979, "0.054410482741556604"], [1714455042.979, "0.054410482741556604"], [1714455043.979, "0.054410482741556604"], [1714455044.979, "0.054410482741556604"], [1714455045.979, "0.054410482741556604"], [1714455046.979, "0.054410482741556604"], [1714455047.979, "0.04163826916321056"], [1714455048.979, "0.04163826916321056"], [1714455049.979, "0.04163826916321056"], [1714455050.979, "0.04163826916321056"], [1714455051.979, "0.052524101462693776"], [1714455052.979, "0.052524101462693776"], [1714455053.979, "0.052524101462693776"], [1714455054.979, "0.052524101462693776"], [1714455055.979, "0.052524101462693776"], [1714455056.979, "0.052524101462693776"], [1714455057.979, "0.052524101462693776"], [1714455058.979, "0.052524101462693776"], [1714455059.979, "0.052524101462693776"], [1714455060.979, "0.052524101462693776"], [1714455061.979, "0.052524101462693776"], [1714455062.979, "0.04505779468008639"], [1714455063.979, "0.030012407042960324"], [1714455064.979, "0.030012407042960324"], [1714455065.979, "0.030012407042960324"], [1714455066.979, "0.030012407042960324"], [1714455067.979, "0.030012407042960324"], [1714455068.979, "0.030012407042960324"], [1714455069.979, "0.030012407042960324"], [1714455070.979, "0.030012407042960324"], [1714455071.979, "0.030012407042960324"], [1714455072.979, "0.030012407042960324"], [1714455073.979, "0.027865688748134568"], [1714455074.979, "0.027865688748134568"], [1714455075.979, "0.027865688748134568"], [1714455076.979, "0.027865688748134568"], [1714455077.979, "0.027865688748134568"], [1714455078.979, "0.027865688748134568"], [1714455079.979, "0.027865688748134568"], [1714455080.979, "0.027865688748134568"], [1714455081.979, "0.027865688748134568"], [1714455082.979, "0.027865688748134568"], [1714455083.979, "0.027865688748134568"], [1714455084.979, "0.027865688748134568"], [1714455085.979, "0.029507289674502703"], [1714455086.979, "0.029507289674502703"], [1714455087.979, "0.029507289674502703"], [1714455088.979, "0.029507289674502703"], [1714455089.979, "0.029507289674502703"], [1714455090.979, "0.03232652587557387"], [1714455091.979, "0.03232652587557387"], [1714455092.979, "0.03232652587557387"], [1714455093.979, "0.03232652587557387"], [1714455094.979, "0.03232652587557387"], [1714455095.979, "0.03232652587557387"], [1714455096.979, "0.03232652587557387"], [1714455097.979, "0.03232652587557387"], [1714455098.979, "0.03232652587557387"], [1714455099.979, "0.03232652587557387"], [1714455100.979, "0.03232652587557387"], [1714455101.979, "0.03232652587557387"], [1714455102.979, "0.03232652587557387"], [1714455103.979, "0.03009045869061575"], [1714455104.979, "0.03009045869061575"], [1714455105.979, "0.03009045869061575"], [1714455106.979, "0.03009045869061575"], [1714455107.979, "0.03009045869061575"], [1714455108.979, "0.03009045869061575"], [1714455109.979, "0.03009045869061575"], [1714455110.979, "0.029228977187810527"], [1714455111.979, "0.029228977187810527"], [1714455112.979, "0.029228977187810527"], [1714455113.979, "0.029228977187810527"], [1714455114.979, "0.029228977187810527"], [1714455115.979, "0.029228977187810527"], [1714455116.979, "0.029228977187810527"], [1714455117.979, "0.029228977187810527"], [1714455118.979, "0.031380717640632994"], [1714455119.979, "0.031380717640632994"], [1714455120.979, "0.031380717640632994"], [1714455121.979, "0.031380717640632994"], [1714455122.979, "0.031380717640632994"], [1714455123.979, "0.030177060576557654"], [1714455124.979, "0.030177060576557654"], [1714455125.979, "0.030177060576557654"], [1714455126.979, "0.030177060576557654"], [1714455127.979, "0.030177060576557654"], [1714455128.979, "0.030177060576557654"], [1714455129.979, "0.02796279109302916"], [1714455130.979, "0.02796279109302916"], [1714455131.979, "0.02796279109302916"], [1714455132.979, "0.02796279109302916"], [1714455133.979, "0.02796279109302916"], [1714455134.979, "0.02796279109302916"], [1714455135.979, "0.02796279109302916"], [1714455136.979, "0.02796279109302916"], [1714455137.979, "0.02796279109302916"], [1714455138.979, "0.02796279109302916"], [1714455139.979, "0.02796279109302916"], [1714455140.979, "0.02796279109302916"], [1714455141.979, "0.10229630106438174"], [1714455142.979, "0.10229630106438174"], [1714455143.979, "0.10229630106438174"], [1714455144.979, "0.10229630106438174"], [1714455145.979, "0.10229630106438174"], [1714455146.979, "0.10229630106438174"], [1714455147.979, "0.10229630106438174"], [1714455148.979, "0.17388626416158157"], [1714455149.979, "0.17388626416158157"], [1714455150.979, "0.17388626416158157"], [1714455151.979, "0.17388626416158157"], [1714455152.979, "0.17388626416158157"], [1714455153.979, "0.17388626416158157"], [1714455154.979, "0.17388626416158157"], [1714455155.979, "0.10537575844539844"], [1714455156.979, "0.10537575844539844"], [1714455157.979, "0.10537575844539844"], [1714455158.979, "0.10537575844539844"], [1714455159.979, "0.10537575844539844"], [1714455160.979, "0.10537575844539844"], [1714455161.979, "0.10537575844539844"], [1714455162.979, "0.10537575844539844"], [1714455163.979, "0.0359821329212573"], [1714455164.979, "0.0359821329212573"], [1714455165.979, "0.0359821329212573"], [1714455166.979, "0.03155228198175272"], [1714455167.979, "0.03155228198175272"], [1714455168.979, "0.03155228198175272"], [1714455169.979, "0.03155228198175272"], [1714455170.979, "0.03155228198175272"], [1714455171.979, "0.03155228198175272"], [1714455172.979, "0.03155228198175272"], [1714455173.979, "0.03155228198175272"], [1714455174.979, "0.03155228198175272"], [1714455175.979, "0.03155228198175272"], [1714455176.979, "0.03155228198175272"], [1714455177.979, "0.03400792756332252"], [1714455178.979, "0.03389316494098144"], [1714455179.979, "0.03389316494098144"], [1714455180.979, "0.03389316494098144"], [1714455181.979, "0.03389316494098144"], [1714455182.979, "0.03389316494098144"], [1714455183.979, "0.03389316494098144"], [1714455184.979, "0.03389316494098144"], [1714455185.979, "0.03389316494098144"], [1714455186.979, "0.03389316494098144"], [1714455187.979, "0.03389316494098144"], [1714455188.979, "0.03389316494098144"], [1714455189.979, "0.03389316494098144"], [1714455190.979, "0.03394308613243484"], [1714455191.979, "0.03394308613243484"], [1714455192.979, "0.03394308613243484"], [1714455193.979, "0.03394308613243484"], [1714455194.979, "0.03394308613243484"], [1714455195.979, "0.03532680650122555"], [1714455196.979, "0.03532680650122555"], [1714455197.979, "0.03532680650122555"], [1714455198.979, "0.03532680650122555"], [1714455199.979, "0.03532680650122555"], [1714455200.979, "0.03532680650122555"], [1714455201.979, "0.03532680650122555"], [1714455202.979, "0.03532680650122555"], [1714455203.979, "0.03532680650122555"], [1714455204.979, "0.03532680650122555"], [1714455205.979, "0.03532680650122555"], [1714455206.979, "0.03532680650122555"], [1714455207.979, "0.041148968681917135"], [1714455208.979, "0.043571286861488874"], [1714455209.979, "0.043571286861488874"], [1714455210.979, "0.043571286861488874"], [1714455211.979, "0.043571286861488874"], [1714455212.979, "0.043571286861488874"], [1714455213.979, "0.043571286861488874"], [1714455214.979, "0.043571286861488874"], [1714455215.979, "0.043571286861488874"], [1714455216.979, "0.043571286861488874"], [1714455217.979, "0.043571286861488874"], [1714455218.979, "0.043571286861488874"]]

# Convert timestamps to numpy datetime64 objects
timestamps = np.array([np.datetime64(datetime.fromtimestamp(ts)) for ts, _ in data])
# Extract values
values = [float(value) for _, value in data]

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(timestamps, values)

# Calculate the start and end times
start_time = np.datetime64('2024-04-30T07:24:00')
end_time = timestamps[-1]

# Calculate the nearest 20-second interval after the start time
start_time = start_time + np.timedelta64(20 - start_time.astype('datetime64[s]').astype(int) % 20, 's')

# Generate a list of ticks every 20 seconds after the start time
ticks = np.arange(start_time, end_time + np.timedelta64(1, 's'), np.timedelta64(20, 's'))

# Convert ticks to seconds since start_time
seconds_since_start = (ticks - start_time) / np.timedelta64(1, 's')

# Set ticks on the x-axis and format as seconds
plt.gca().set_xticks(ticks)
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:g}s'.format(x - start_time.astype('datetime64[s]').astype(int))))

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Plot with Timestamps every 20 seconds (starting at 7:24)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()